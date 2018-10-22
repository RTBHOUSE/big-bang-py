"""
Initialize Big-Bang-py in your project.

Repo: https://github.com/rtbhouse/big-bang-py
"""

import subprocess
from urllib.request import urlretrieve

if __name__ == '__main__':
    urlretrieve(
        url='https://raw.githubusercontent.com/rtbhouse/big-bang-py/master/tasks.py',
        filename='tasks.py',
    )
    subprocess.run(['git', 'init'])  # Git init is necessary to copy pre-commit Git hook
    subprocess.run(['pipenv', 'install', 'invoke'])
    subprocess.run(['pipenv', 'run', 'invoke', 'update-big-bang-files'])
