import os

from constants import PROJECT_ROOT
from envs.loader import load_envs


def test_load_envs(mocker, monkeypatch):
    # GIVEN
    load_dotenv_mock = mocker.patch('envs.loader.load_dotenv')
    monkeypatch.setenv('ENV_FILE_NAME', 'dummy.env')

    # WHEN
    load_envs()

    # THEN
    env_file_path = PROJECT_ROOT / 'envs' / 'dummy.env'
    load_dotenv_mock.assert_called_once_with(env_file_path, override=True)
    assert os.environ['ENV_FILE_PATH'] == str(env_file_path)
