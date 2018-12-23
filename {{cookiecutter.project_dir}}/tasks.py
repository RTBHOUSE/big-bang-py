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
def set_precommit(c):
    """
    Setup pre-commit Git hook saved in `$PROJECT_ROOT/githooks/pre-commit`.
    """
    c.run(
        'cp githooks/pre-commit .git/hooks/pre-commit '
        '&& chmod +x .git/hooks/pre-commit'
        '&& git config --bool flake8.strict true',
        pty=True
    )


@invoke.task
def linters(c):
    """Lint source code using Isort, YAPF and Flake8 (with various plugins)."""
    logger.info('')
    logger.info('###############################')
    logger.info('# Sort Python imports (Isort) #')
    logger.info('###############################')
    logger.info('')
    c.run('python -m isort --apply --quiet', pty=True)

    logger.info('#####################################')
    logger.info('# Enforce Python style guide (YAPF) #')
    logger.info('#####################################')
    logger.info('')
    c.run('python -m yapf --in-place --recursive .', pty=True)

    logger.info('####################################')
    logger.info('# Apply dozens of linters (Flake8) #')
    logger.info('####################################')
    logger.info('')
    c.run('python -m flake8', pty=True)


@invoke.task
def tests(c):
    """Run pytests with coverage report."""
    c.run('python -m pytest --cov={{ cookiecutter.project_source_code_dir }} --cov=envs --cov-branch', pty=True)


##################################
# Organise tasks into namespaces #
##################################

# The main namespace MUST be named `namespace` or `ns`.
# See: http://docs.pyinvoke.org/en/1.2/concepts/namespaces.html
namespace = invoke.Collection()

namespace.add_task(coverage_report)
namespace.add_task(flake8_report)
namespace.add_task(linters)
namespace.add_task(tests)

githooks_namespace = invoke.Collection('githooks')
githooks_namespace.add_task(set_precommit)
namespace.add_collection(githooks_namespace)
