import logging.config
import random
import shutil
import string

from invoke import task

from src.logging_config import DICT_CONFIG

logging.config.dictConfig(DICT_CONFIG)
logger = logging.getLogger('main')


@task
def coverage_report(c):
    """Open refreshed coverage report in a browser."""
    c.run('coverage html && open htmlcov/index.html', pty=True)


@task
def flake8_report(c):
    """Open refreshed Flake8 report in a browser."""
    c.run('flake8 --format=html --htmldir=flake-report; open flake-report/index.html', pty=True)


@task
def install_precommit(c):
    """Install pre-commit githook."""
    c.run('cp hooks/pre-commit .git/hooks/pre-commit && chmod +x .git/hooks/pre-commit', pty=True)


@task
def linters(c):
    """Lint source code using Isort, YAPF and Flake8 (with various plugins)."""
    logger.info('')
    logger.info('###################################')
    logger.info('# Isort - Sort Yer Python Imports #')
    logger.info('###################################')
    logger.info('')
    c.run('isort --apply --quiet', pty=True)

    logger.info('#######################################')
    logger.info('# YAPF - Yet Another Python Formatter #')
    logger.info('#######################################')
    logger.info('')
    c.run('yapf --in-place --recursive .', pty=True)

    logger.info('#################################')
    logger.info('# Flake8 & Happy Plugins Family #')
    logger.info('#################################')
    logger.info('')
    c.run('flake8', pty=True)


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
            '.flake8',
            '.gitignore',
            '.isort.cfg',
            '.style.yapf',
            'Pipfile',
            'pytest.ini',
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
