# Changelog

## Unreleased

+ Bugs:

    + Replace 'src' with '{{ cookiecutter.project_source_code_dir }}'.
    
    + Change .version to '0.0.0' to fix 'make-release' Invoke task.


## 0.1.0 - 2019-05-06

+ Manage dependencies with pip-tools instead of Pipenv.
 
+ Add Invoke tasks to automate making a release.

+ Integrate Pre-commit Git Hook with CI script.

+ Refactor setup scripts.

+ Refactor utilities and add <humanize_seconds>.

+ Rename folder \<constants> to \<dirs>.

+ Add Bandit.

+ Add CHANGELOGs.

+ Update flake8 to base on double quotes.

+ Refactor cowsays! Moo!

