# Big-Bang-py

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for Python projects. RTB House flavor.

##Features

+ Automatic setup via `./finish_project_setup` script, which: 

    + Installs app dependencies via Pipenv.
    
    + Installs Invoke Bash completion.
    
    + Initializes git and makes first commit.
    
    + Installs pre-commit and triggers it to check if it works properly.
    
    + Loads Pipenv shell, so you can start straight away.

+ Configured .gitignore.

+ Configured YAPF.

+ Configured isort.

+ Configured Flake8.

+ Configured logging.

+ Basic Invoke tasks.

+ Basic project structure (`main.py`, `source_code_dir`, `tests`, `envs`).

+ README skeleton.

## Requirements

+ [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter)

+ [Pipenv](https://pipenv.readthedocs.io/en/latest/install/#installing-pipenv)


## Usage

+ Generate a new project from command line by calling `cookiecutter gh:RTBHOUSE/big-bang-py`.

+ Answer all of the prompted questions.

+ Run `./finish_project_setup` script.

+ And Voilà! You're ready to code!


## License

This Cookiecutter is licensed under the terms of the [MIT License](/LICENSE).
