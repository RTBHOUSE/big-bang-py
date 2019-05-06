import invoke

from src.utils import cowsay


@invoke.task
def coverage_report(c):
    """Open refreshed coverage report in a browser."""
    c.run(
        command=(
            "coverage combine .coverage "  # Necessary to translate Docker to local source files.
            "&& coverage html "
            "&& open htmlcov/index.html"
        ),
        pty=True,
    )


@invoke.task
def flake8_report(c):
    """Open refreshed Flake8 report in a browser."""
    c.run(
        command=(
            "python -m flake8 --format=html --htmldir=flake-report; "
            "open flake-report/index.html"
        ),
        pty=True
    )


@invoke.task
def linters(c):
    """Lint source code using Isort, YAPF, Flake8 and Bandit."""
    cowsay("Isort - Sort Yer Python Imports", print_end="\n")
    c.run("python -m isort --apply --quiet", pty=True)

    cowsay("YAPF - Yet Another Python Formatter", print_end="\n")
    c.run("python -m yapf --in-place --recursive ci/ envs/ githooks/ src/ tasks/ tests/", pty=True)

    cowsay("Flake8 & Happy Plugins Family", print_end="\n")
    c.run("python -m flake8", pty=True)

    cowsay("Find security issues with Bandit")
    c.run("bandit --recursive .")
    print("")


@invoke.task
def set_precommit(c):
    """Set Pre-commit Git Hook saved in `./githooks/pre-commit`."""
    c.run(
        command=(
            "ln -sf ../../githooks/pre-commit .git/hooks/pre-commit "
            # Make Flake8 failures prevent commits.
            "&& git config --bool flake8.strict true"
        ),
        pty=True
    )


@invoke.task
def run_tests(c, tests="tests"):
    """Run pytests with coverage report."""
    c.run(f"python -m pytest {tests} --cov=src --cov-branch", pty=True)
