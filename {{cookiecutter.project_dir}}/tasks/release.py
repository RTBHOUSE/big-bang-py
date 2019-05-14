import re
import sys
from datetime import date

import invoke

from {{ cookiecutter.project_source_code_dir }}.utils import cowsay


@invoke.task(help={"type": "[REQUIRED] Allowed values: 'major', 'minor', 'patch'."})
def make_release(c, type_):
    """Make a new release - update files, make & tag commit, push to origin."""
    _validate_release_type(type_)
    _ask_if_changelog_is_ready()
    new_version = _calculate_new_version(type_)
    _update_version_in_files(new_version)
    _commit_tag_and_push_new_release(c, new_version)


def _ask_if_changelog_is_ready():
    question = (
        "\n"
        "Is 'Unreleased' section of CHANGELOG.md final or ready to be commited "
        "as a new release? (y/n): "
    )
    answer = input(question)
    changelog_is_ready = answer.lower() in {"y", "yes", "yep", "si"}
    if not changelog_is_ready:
        print()
        print("Go on and prepare CHANGELOG.md, then!")
        print()
        sys.exit(1)


def _validate_release_type(type_):
    valid_release_types = ["major", "minor", "patch"]
    if type_ not in valid_release_types:
        raise ValueError(
            f"Release type '{type_}' is invalid! "
            f"Please choose from: {str(valid_release_types)[1:-1]}"
        )


def _calculate_new_version(type_):
    cowsay("Calculate New App Version", print_end="\n")

    with open(".version") as version_file:
        current_version = version_file.readline().strip()

    major, minor, patch = map(int, current_version.split("."))

    if type_ == "major":
        major += 1
        minor = 0
        patch = 0
    elif type_ == "minor":
        minor += 1
        patch = 0
    elif type_ == "patch":
        patch += 1
    else:
        raise RuntimeError(f"Unhandled type_={type_}! This should not happen!")

    new_version = f"{major}.{minor}.{patch}"
    return new_version


def _update_version_in_files(new_version):
    cowsay("Update App Version In Files")

    with open(".version", mode="w") as version_file:
        version_file.write(new_version)

    with open("CHANGELOG.md", "r+") as changelog_file:
        changelog = changelog_file.read()
        changelog = re.sub(
            pattern="## Unreleased",
            repl=f"## {new_version} - {str(date.today())}",
            string=changelog,
        )
        changelog_file.seek(0)
        changelog_file.write(changelog)
        changelog_file.truncate()


def _commit_tag_and_push_new_release(c, new_version):
    cowsay("Commit New Release", print_end="\n")
    c.run(command="git add .version CHANGELOG.md", pty=True)
    c.run(command=f"git commit -m 'Release {new_version}'", pty=True)

    cowsay("Tag New Release")
    c.run(command=f"git tag {new_version}", pty=True)

    cowsay("Push New Release")
    c.run(command=f"git push origin master {new_version}", pty=True)
