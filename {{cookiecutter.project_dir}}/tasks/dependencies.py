import invoke


@invoke.task
def compile_(c):
    """Compile dependencies using pip-tools (https://github.com/jazzband/pip-tools)."""
    c.run(
        "pip-compile "
        "--upgrade "
        "--generate-hashes "
        "--output-file requirements/locked/base.txt "
        "requirements/abstract/base.in"
    )
    print("")
    c.run(
        "pip-compile "
        "--upgrade "
        "--generate-hashes "
        "--output-file requirements/locked/dev.txt "
        "requirements/abstract/dev.in"
    )
    print("")


@invoke.task
def sync_dev(c):
    """Synchronise dependencies i.e. delete OLD, update EXISTING & install NEW."""
    c.run("pip-sync requirements/locked/dev.txt")
    print("")
