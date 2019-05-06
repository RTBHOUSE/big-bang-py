# Big-Bang-py

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for Python projects. RTB House flavor.


## Features

+ Automatic setup via one-liner (see section [Usage](#usage)), which: 

    + Loads virtualenv, so you can start straight away.
    
    + Installs Invoke Bash tab-completion.
    
    + Installs app dependencies with help of [pip-tools](https://github.com/jazzband/pip-tools).
    
    + Initializes git repository and makes first commit.
    
    + Installs pre-commit and checks if it works.

+ Configured .gitignore.

+ Configured Bandit.

+ Configured Flake8.

+ Configured isort.

+ Configured logging.

+ Configured YAPF.

+ Ready-to-go CI script.

+ Basic Invoke tasks (**including automation of making a release!**)

+ Basic project structure (`main.py`, `source_code_dir`, `requirements`, `tests`, etc.).

+ README & CHANGELOG skeleton.


## Requirements

+ [Cookiecutter](https://cookiecutter.readthedocs.io/en/latest/installation.html#install-cookiecutter)

+ [virtualenv](https://virtualenv.pypa.io/en/latest/installation/)


## Usage

```console
# Generate a new project.
> cookiecutter gh:RTBHOUSE/big-bang-py

# Answer all of the prompted questions.
# Brackets show default options. Click <enter> if you wish to accept them.
project_name [My New Project]: ???
project_dir  [my-new-project]: ???
project_source_code_dir [src]: ???

# Finish with:
> cd $MY_NEW_PROJECT_DIR
> virtualenv venv \
    && ./invoke_bash_completion \
    && source venv/bin/activate \
    && pip install invoke pip-tools \
    && ./finish_project_setup
```

And voilà! You are ready to code!


## License

This Cookiecutter is licensed under the terms of the [MIT License](/LICENSE).
