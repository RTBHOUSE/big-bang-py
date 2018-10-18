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
def linters(c):
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
    c.run('python run_mccabe.py 7', pty=True)
    print('')


@task(post=[install_precommit])
def update_big_bang_files(c):
    """
    Update selected files (and dirs) based on the local clone of Big-Bang-py.

    Repo: https://bitbucket.org/rtbhouse/big-bang-py
    """
    check_if_big_bang_py_dir_env_exists()
    copy_from_big_bang_py_to_local_dir(
        c,
        file_or_dir_names=[
            # dirs
            'envs',
            'hooks',
            'tests',
            # files
            '.gitignore',
            '.isort.cfg',
            '.style.yapf',
            'Pipfile',
            'pytest.ini',
            'run_mccabe.py',
        ]
    )


@task
def tests(c):
    """Run pytests with coverage report."""
    c.run('python -m pytest --cov=src --cov=envs --cov-branch', pty=True)


def check_if_big_bang_py_dir_env_exists():
    if 'BIG_BANG_PY_DIR' not in os.environ:
        raise RuntimeError(
            'Please setup `BIG_BANG_PY_DIR` ENV holding full path to the local '
            'copy of Big-Bang-py (https://bitbucket.org/rtbhouse/big-bang-py).'
        )


def copy_from_big_bang_py_to_local_dir(c, file_or_dir_names):
    for name in file_or_dir_names:
        c.run(f'cp -R $BIG_BANG_PY_DIR/{name} .', pty=True)
