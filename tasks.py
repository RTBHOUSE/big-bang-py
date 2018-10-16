import os

from invoke import task


@task
def coverage(c):
    """Open refreshed coverage report in a browser."""

    c.run('coverage html && open htmlcov/index.html', pty=True)


@task
def install_precommit(c):
    """Install pre-commit githook."""

    c.run('cp hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit', pty=True)


@task
def job(c):
    """
    Run job doing X, Y and Z.
    """

    c.run('python ./job.py', pty=True)


@task
def lint(c):
    """Lint source code using YAPF and isort."""

    print('')
    print('#######################################')
    print('# YAPF - Yet Another Python Formatter #')
    print('#######################################')
    print('')
    c.run('python -m yapf --version', pty=True)
    c.run('python -m yapf --in-place --recursive .', pty=True)

    c.run('python -m isort --version', pty=True)
    c.run('python -m isort --apply', pty=True)

@task
def update_gitignore(c):
    """Update .gitignore."""

    if 'BIG_BANG_PY_DIR' not in os.environ:
        raise RuntimeError(
            'Please setup `BIG_BANG_PY_DIR` ENV pointing to the local copy '
            'of Big-Bang-py (https://bitbucket.org/rtbhouse/big-bang-py).'
        )
    c.run('cp $BIG_BANG_PY_DIR/.gitignore .', pty=True)


@task
def tests(c):
    """Run pytests."""

    c.run('python -m pytest --cov=src --cov=envs --cov-branch', pty=True)
