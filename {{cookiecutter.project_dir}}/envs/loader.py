import os

from dotenv import load_dotenv

from dirs import PROJECT_ROOT


def load_envs() -> None:
    """Load ENVs from $PROJECT_ROOT/envs/$ENV_FILE_NAME."""
    env_file_name = os.environ["ENV_FILE_NAME"]
    env_file_path = PROJECT_ROOT / "envs" / env_file_name
    load_dotenv(env_file_path, override=True)
    # Set below ENV for easy access in logging, debugging etc.
    os.environ["ENV_FILE_PATH"] = str(env_file_path)
