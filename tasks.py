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
def update_isort(c):
    """
    Update `.isort.cfg` by copying the version from the local clone of repo
    Big-Bang-py (https://bitbucket.org/rtbhouse/big-bang-py).
    """

    check_if_big_bang_py_dir_env_exists()
    c.run('cp $BIG_BANG_PY_DIR/.isort.cfg .', pty=True)


@task
def update_yapf(c):
    """Update .style.yapf."""

    if 'BIG_BANG_PY_DIR' not in os.environ:
        raise RuntimeError(
            'Please setup `BIG_BANG_PY_DIR` ENV pointing to the local copy '
            'of Big-Bang-py (https://bitbucket.org/rtbhouse/big-bang-py).'
        )
    c.run('cp $BIG_BANG_PY_DIR/.style.yapf .', pty=True)


@task
def tests(c):
    """Run pytests."""

    c.run('python -m pytest --cov=src --cov=envs --cov-branch', pty=True)

def check_if_big_bang_py_dir_env_exists():
    if 'BIG_BANG_PY_DIR' not in os.environ:
        raise RuntimeError(
            'Please setup `BIG_BANG_PY_DIR` ENV holding full path to the local '
            'copy of Big-Bang-py (https://bitbucket.org/rtbhouse/big-bang-py).'
        )
