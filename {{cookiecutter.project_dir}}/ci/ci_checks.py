#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess  # nosec
import sys

from flake8.main import git
from isort.hooks import git_hook as isort_githook

from {{ cookiecutter.project_source_code_dir }}.utils import cowsay


def run_ci_checks():
    _run_pytests()
    _check_imports_order_with_isort()
    _check_code_formatting_with_yapf()
    _check_code_style_with_flake8()
    _check_security_issues_with_bandit()
    _check_python_packages_safety()


def _run_pytests():
    cowsay("Run tests")
    pytests_cmd = ["invoke", "run-tests"]
    tests_return_code = subprocess.run(pytests_cmd).returncode  # nosec
    # Exit code 0: All tests were collected and passed successfully.
    # Exit code 5: No tests were collected.
    if tests_return_code not in {0, 5}:
        print("")
        print(f"Tests Exit Status: {tests_return_code} => aborting commit!")
        sys.exit(tests_return_code)


def _check_imports_order_with_isort():
    cowsay("Import Order Check")
    isort_exit_status = isort_githook(strict=True)
    if isort_exit_status == 0:
        print("Isort Exit Status: 0 => OK!")
    else:
        sys.exit(isort_exit_status)


def _check_code_formatting_with_yapf():
    cowsay("Code Formatting Check (YAPF)")
    yapf_cmd = [
        "yapf", "--recursive", "--diff", "ci/", "envs/", "githooks/", "{{ cookiecutter.project_source_code_dir }}/", "tasks/", "tests/"
    ]
    yapf_return_code = subprocess.run(yapf_cmd).returncode  # nosec
    if yapf_return_code == 0:
        print("YAPF Exit Status: 0 => OK!")
    else:
        print("")
        print(f"YAPF Exit Status: {yapf_return_code} => aborting commit!")
        print("")
        sys.exit(yapf_return_code)


def _check_code_style_with_flake8():
    cowsay("Flake8 Style Guide Enforcement")
    flake8_return_code = git.hook(
        strict=git.config_for("strict"),
        lazy=git.config_for("lazy"),
    )
    if flake8_return_code == 0:
        print("Flake8 Exit Status: 0 => OK!")
        print("")
    else:
        print("")
        print(f"Flake8 Exit Status: {flake8_return_code} => aborting commit!")
        print("")
        sys.exit(flake8_return_code)


def _check_security_issues_with_bandit():
    cowsay("Find security issues with Bandit")
    bandit_command = ["bandit", "--recursive", "."]
    bandit_return_code = subprocess.run(bandit_command).returncode  # nosec
    if bandit_return_code == 0:
        print("Bandit Exit Status: 0 => OK!")
    else:
        print("")
        print(f"Bandit Exit Status: {bandit_return_code} => aborting commit!")
        print("")
        sys.exit(bandit_return_code)


def _check_python_packages_safety():
    cowsay("Check Python Packages Safety")
    safety_command = ["safety", "check", "--file", "requirements/locked/dev.txt"]
    safety_return_code = subprocess.run(safety_command).returncode  # nosec
    if safety_return_code == 0:
        print("")
        print("Safety Exit Status: 0 => OK!")
    else:
        print("")
        print(f"Safety Exit Status: {safety_return_code} => aborting commit!")
        sys.exit(safety_return_code)


if __name__ == "__main__":
    run_ci_checks()
