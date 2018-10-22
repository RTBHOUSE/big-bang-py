import random
import shutil
import string

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
    Update selected files (including files in dirs) from Big-Bang-py repo.

    Repo: https://github.com/rtbhouse/big-bang-py
    """

    big_bang_py_temp_dir = get_random_string(length=40)
    try:
        c.run(f'git clone git@github.com:rtbhouse/big-bang-py.git {big_bang_py_temp_dir}')
        files_and_dirs_to_copy = [
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
        for asset in files_and_dirs_to_copy:
            c.run(f'cp -R {big_bang_py_temp_dir}/{asset} .', pty=True)
    finally:
        shutil.rmtree(big_bang_py_temp_dir)


@task
def tests(c):
    """Run pytests with coverage report."""
    c.run('python -m pytest --cov=src --cov=envs --cov-branch', pty=True)


def get_random_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
