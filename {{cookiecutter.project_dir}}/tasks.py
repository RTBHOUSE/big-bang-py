import logging.config

import invoke

from {{ cookiecutter.project_source_code_dir }}.logging_config import DICT_CONFIG

logging.config.dictConfig(DICT_CONFIG)
logger = logging.getLogger('main')


@invoke.task
def coverage_report(c):
    """Open refreshed coverage report in a browser."""
    c.run('coverage html && open htmlcov/index.html', pty=True)


@invoke.task
def flake8_report(c):
    """Open refreshed Flake8 report in a browser."""
    c.run(
        'python -m flake8 --format=html --htmldir=flake-report; '
        'open flake-report/index.html',
        pty=True
    )


@invoke.task
def install_precommit(c):
    """Install pre-commit githook."""
    c.run(
        'cp hooks/pre-commit .git/hooks/pre-commit '
        '&& chmod +x .git/hooks/pre-commit'
        '&& git config --bool flake8.strict true',
        pty=True
    )


@invoke.task
def linters(c):
    """Lint source code using Isort, YAPF and Flake8 (with various plugins)."""
    logger.info('')
    logger.info('######################################')
    logger.info('# Isort - Sort Imports Automatically #')
    logger.info('######################################')
    logger.info('')
    c.run('python -m isort --apply --quiet', pty=True)

    logger.info('#####################################')
    logger.info('# YAPF - Enforce Python Style Guide #')
    logger.info('#####################################')
    logger.info('')
    c.run('python -m yapf --in-place --recursive .', pty=True)

    logger.info('####################################')
    logger.info('# Flake8 - Apply Dozens of Linters #')
    logger.info('####################################')
    logger.info('')
    c.run('python -m flake8', pty=True)


@invoke.task
def tests(c):
    """Run pytests with coverage report."""
    c.run('python -m pytest --cov={{ cookiecutter.project_source_code_dir }} --cov=envs --cov-branch', pty=True)
