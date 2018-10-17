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
def lint(c):
    """Lint source code using YAPF, Isort and McCabe."""

    print('')
    print('#######################################')
    print('# YAPF - Yet Another Python Formatter #')
    print('#######################################')
    print('')
    c.run('python -m yapf --version', pty=True)
    c.run('python -m yapf --in-place --recursive .', pty=True)

    c.run('python -m isort --version', pty=True)
    c.run('python -m isort --apply', pty=True)

    print('')
    print('####################################')
    print('# McCabe - Code Complexity Checker #')
    print('####################################')
    print('')
    c.run('python run-mccabe.py 7', pty=True)


@task
def setup_big_bang_py(c):
    """
    Setup Big-Bang-py files and dirs.

    In fact, copy their version from the local clone of repo Big-Bang-py
    (https://bitbucket.org/rtbhouse/big-bang-py).
    """
    check_if_big_bang_py_dir_env_exists()
    copy_from_big_bang_py_to_local_dir(c, file_or_dir_names=[
        '.isort.cfg',
        '.style.yapf',
        'envs',
        'pytest.ini',
        'run-mccabe.py',
        'tasks.py',
    ])


@task
def tests(c):
    """Run pytests with coverage report."""

    c.run('python -m pytest --cov=src --cov-branch', pty=True)


def check_if_big_bang_py_dir_env_exists():
    if 'BIG_BANG_PY_DIR' not in os.environ:
        raise RuntimeError(
            'Please setup `BIG_BANG_PY_DIR` ENV holding full path to the local '
            'copy of Big-Bang-py (https://bitbucket.org/rtbhouse/big-bang-py).'
        )


def copy_from_big_bang_py_to_local_dir(c, file_or_dir_names):
    for name in file_or_dir_names:
        c.run(f'cp -R $BIG_BANG_PY_DIR/{name} .', pty=True)
