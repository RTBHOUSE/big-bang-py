#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Initialize Big-Bang-py in your project.

+ Copy files and dirs from the local clone of Big-Bang-py repo.
+ Install necessary packages using Pipenv.
+ Initialize Git repository.
+ Install pre-commit Git-hook.

Repo: https://bitbucket.org/rtbhouse/big-bang-py
"""

import os
import subprocess
from pathlib import Path

try:
    big_bang_tasks_file = Path(os.environ['BIG_BANG_PY_DIR']) / 'tasks.py'
except KeyError:
    raise RuntimeError(
        'Please setup `BIG_BANG_PY_DIR` ENV holding full path to the local '
        'copy of Big-Bang-py (https://bitbucket.org/rtbhouse/big-bang-py).'
    )
subprocess.run(['cp', '-R', big_bang_tasks_file, '.'])
subprocess.run(['pipenv', 'install', 'invoke'])
subprocess.run(['git', 'init'])
subprocess.run(['pipenv', 'run', 'invoke', 'update-big-bang-files'])
