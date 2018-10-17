import os
from pathlib import Path

from dotenv import load_dotenv


def load_envs() -> None:
    """
    Loads ENVs from $PROJECT_ROOT/envs/$ENV_FILE_NAME.

    One of the ways to preload `ENV_FILE_NAME` ENV is to use `pipenv shell` or
    `pipenv run`, which automatically load ENVs from `$PROJECT_ROOT/.env` file:
    https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-automatic-loading-of-env
    """
    project_root = Path(__file__).parent.parent
    env_file_name = os.environ['ENV_FILE_NAME']
    env_file_path = project_root / 'envs' / env_file_name
    load_dotenv(env_file_path, override=True)
    # Set below ENV for easy access in logging, debugging etc.
    os.environ['ENV_FILE_PATH'] = str(env_file_path)
