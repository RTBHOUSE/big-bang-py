# Big-Bang-py

[Cookiecutter](https://github.com/audreyr/cookiecutter) template for Python projects. RTB House flavor.


## Features

+ Automatic setup via `./finish_project_setup` script, which: 

    + Installs app dependencies via Pipenv.
    
    + Installs Invoke Bash completion.
    
    + Initializes git and makes first commit.
    
    + Installs pre-commit and checks if it works.
    
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

```console
# Generate a new project.
$ cookiecutter gh:RTBHOUSE/big-bang-py

# Answer all of the prompted questions.
# Brackets show default options. Click <enter> if you wish to accept them.
project_name [My New Project]: ???
project_dir  [my-new-project]: ???
project_source_code_dir [src]: ???

# Finish with:
$ cd $MY_NEW_PROJECT_DIR
$ ./finish_project_setup
$ ./invoke_bash_completion \
      && rm -f invoke_bash_completion \
      && source $VIRTUAL_ENV/bin/activate

```

And voilà! You are ready to code!


## License

This Cookiecutter is licensed under the terms of the [MIT License](/LICENSE).
