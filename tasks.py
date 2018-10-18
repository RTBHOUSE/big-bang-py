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
    c.run('python -m yapf --in-place --recursive .', pty=True)

    print('###################################')
    print('# Isort - Sort Yer Python Imports #')
    print('###################################')
    print('')
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
    if 'BIG_BANG_PY_DIR' not in os.environ:
        raise RuntimeError(
            'Please setup `BIG_BANG_PY_DIR` ENV holding full path to the local '
            'copy of Big-Bang-py (https://bitbucket.org/rtbhouse/big-bang-py).'
        )
    files_and_dirs = [
        # dirs
        'envs',
        'hooks',
        'src',
        'tests',
        # files
        '.gitignore',
        '.isort.cfg',
        '.style.yapf',
        'Pipfile',
        'pytest.ini',
        'run_mccabe.py',
    ]
    for asset in files_and_dirs:
        c.run(f'cp -R $BIG_BANG_PY_DIR/{asset} .', pty=True)


@task
def tests(c):
    """Run pytests with coverage report."""
    c.run('python -m pytest --cov=src --cov=envs --cov-branch', pty=True)
