import os

from dotenv import load_dotenv

from constants import PROJECT_ROOT


def load_envs() -> None:
    """
    Load ENVs from $PROJECT_ROOT/envs/$ENV_FILE_NAME.

    One of the ways to preload `ENV_FILE_NAME` ENV is to use `pipenv shell` or
    `pipenv run`, which automatically load ENVs from `$PROJECT_ROOT/.env` file:
    https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-automatic-loading-of-env
    """
    env_file_name = os.environ['ENV_FILE_NAME']
    env_file_path = PROJECT_ROOT / 'envs' / env_file_name
    load_dotenv(env_file_path, override=True)
    # Set below ENV for easy access in logging, debugging etc.
    os.environ['ENV_FILE_PATH'] = str(env_file_path)
