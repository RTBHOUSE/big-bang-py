# Big-Bang-py

+ Big-Bang-py holds opinionated best practices, scripts & configs to template your next Python project.

+ The content of this repo is based on the research, experience and pure opinions of the authors.

+ The goal is to gather the sweetest & most impactful nuggets of Python projects wisdom and make them accessible from a single place. 

+ Hopefully, Big-bang-py will inspire you to code your awesome projects faster and to make them even better.


## TL;DR Checklist

- Python:

    - Use [Python 3.7](https://docs.python.org/3/whatsnew/3.7.html).
    
    - Manage app dependencies using [Pipenv](https://pipenv.readthedocs.io/en/latest).
    
    - Sort imports with [Isort](https://github.com/timothycrosley/isort).
    
    - Format source files with [YAPF](https://github.com/google/yapf).
    
    - Lint code with [Flake8](https://github.com/PyCQA/flake8).
    
    - Use [pytest](https://docs.pytest.org/en/latest/) as test framework.

- Git:

    - Use [.gitignore](https://git-scm.com/docs/gitignore).
    
    - Use [pre-commit Git hook](https://github.com/RTBHOUSE/big-bang-py/tree/master/hooks/pre-commit).

- Project:

    - Store config (credentials, secrets, etc.) in [ENVs](https://12factor.net/config).
    
    - Manage and execute command line tasks via [Invoke](http://www.pyinvoke.org).
    
    - [Log, log, log.](https://realpython.com/python-logging/)
    
    - Maintain up-to-date [README](https://www.makeareadme.com).
    
    - Set up [Continuous Integration](https://docs.microsoft.com/en-us/azure/devops/learn/what-is-continuous-integration).


## Table of Contents

#### Repo

* [Initialization & Update](#initialization--update)

#### Python

* [Python version](#python-version)
* [Pipenv - App Package Manager](#pipenv---app-package-manager)
* [Isort - Imports Sorter](#isort---imports-sorter)
* [YAPF - Files Formatter](#yapf---files-formatter)
* [Flake8 - Octo-Ninja Linter](#flake8---octo-ninja-linter)
* [McCabe - Code Complexity Checker](#mccabe---code-complexity-checker)
* [Pytest - Test Framework](#pytest---test-framework)

#### Git

* [.gitignore](#gitignore)
* [Pre-commit Git Hook](#pre-commit-git-hook)

#### Project

* [Store config in ENVs](#store-config-in-envs)
* [Invoke - Manage & Execute Tasks](#invoke---manage--execute-tasks)
* [Logging Is A Programmer's Best Friend](#logging-is-a-programmers-best-friend)
* [README - Gateway to Your Code](#readme---gateway-to-your-code)
* [Continuous Integration - Kill Bugs Fast](#continuous-integration---kill-bugs-fast)


## Initialization & Update

- To initialize Big-Bang-py in your project, run [start_big_bang.py](https://github.com/RTBHOUSE/big-bang-py/tree/master/start_big_bang.py) script in the target directory. The script is dependent on `git` and `Pipenv`.
    
- If you wish to simply update some of the files, adjust & run Invoke task [update_big_bang_files]((https://github.com/RTBHOUSE/big-bang-py/tree/master/tasks.py)).
    

## Python version

- **It is recommended to use Python 3.7.**

- There is an informative summary of new features on [Real Python](https://realpython.com/python37-new-features). More detailed description can be found in the [official documentation](https://docs.python.org/3/whatsnew/3.7.html).

- To name some notable additions:

    - [Data Classes](https://realpython.com/python-data-classes) can easily replace [namedtuples](https://docs.python.org/3.7/library/collections.html#collections.namedtuple) and [attrs](https://github.com/python-attrs/attrs).
    
    - [Typing Forward Reference](https://realpython.com/python37-new-features/#typing-enhancements) makes type hints even more programmer-friendly.

    - The `asyncio` module has received many [new features along with usability and performance improvements](https://tryexceptpass.org/article/asyncio-in-37/). For instance,  new `asyncio.run()` automatically creates an event loop, runs a task on it and finally closes the loop when the task is done.
    
- Nonetheless, if you still use previous version of Python (especially 3.6), it is possible to backport some of the new features e.g. [Data Classes](https://github.com/ericvsmith/dataclasses).


## Pipenv - App Package Manager

- **Use [Pipenv](https://pipenv.readthedocs.io/en/latest) to manage Python [app dependencies](https://pipenv.readthedocs.io/en/latest/advanced/#pipfile-vs-setup-py).**
  
- Pipenv consolidates `pip` & `virtualenv` while offering powerful new features. Among others:

    - Virtual environment is created and managed automatically.
    
    - Project dependencies are installed using `Pipfile` (building from the latest allowed versions of packages) or `Pipfile.lock` (making build deterministic):
    
        - `Pipfile` specifies only the packages you need, as those are abstract dependency declarations. Sub-dependencies are taken care of by Pipenv.
        
        - `Pipfile.lock` uses hashes to lock all of the dependencies (including sub-dependencies). This ensures repeatable, deterministic builds. You never manage this file by hand, leaving the matter for Pipenv.
   
- Essential commands:

    - `install` - installs provided packages and adds them to Pipfile. If no packages are given, installs all packages from `Pipfile`.

    - `sync` - deterministic build! Installs all packages specified in `Pipfile.lock`.
    
    - `shell` - spawns a shell with the virtualenv activated.
    
        - [Shell environment will be automatically updated with ENVs from `.env` file](https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-automatic-loading-of-env).
    
    - `run` - runs a given command from the virtualenv with forwarded arguments.
    
        - [Shell environment will be automatically updated with ENVs from `.env` file](https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-automatic-loading-of-env).
    
    - `graph` - shows a dependency graph of the installed dependencies.
    
    - `check` - most importantly, checks for security vulnerabilities.

- You can educate yourself further by reading [Real Python's guide](https://realpython.com/pipenv-guide). It is also recommended to go through [the official documentation](https://pipenv.readthedocs.io/en/latest/#further-documentation-guides).

- **Pipfile with the packages necessary to run all the content of Big-Bang-py may be found in this repo's [Pipfile](https://github.com/RTBHOUSE/big-bang-py/tree/master/Pipfile).**


## Isort - Imports Sorter

- **[Isort](https://github.com/timothycrosley/isort) automatically sorts Python imports in alphabetical order and also groups imports into defined sections.**

- There are several knobs configuring Isort's behavior. Full reference of settings can be found [here](https://github.com/timothycrosley/isort/wiki/isort-Settings#full-reference-of-isort-settings).

- You can specify project level configuration simply by placing `.isort.cfg` file at the root of your project.

    - You may find pre-configured [.isort.cfg](https://github.com/RTBHOUSE/big-bang-py/tree/master/.isort.cfg) at the root of this repo.
    
- It is recommended to include Isort in your linting Invoke task and also to run it during pre-commit Git hook. Example of both can be found in this repo, see [tasks.py](https://github.com/RTBHOUSE/big-bang-py/tree/master/tasks.py) and [pre-commit](https://github.com/RTBHOUSE/big-bang-py/tree/master/hooks/pre-commit).

- To manage edge cases, [disable Isort per line or for entire file](https://github.com/timothycrosley/isort#skip-processing-of-imports-outside-of-configuration).


## YAPF - Files Formatter

- **[YAPF](https://github.com/google/yapf) is a Python files formatter. Its goal is to make the code look as good as written by a programmer who is rigorously following a style guide.**

- The formatting style used by YAPF is configurable, where specific configuration can be pointed in a couple of ways.

    - It is recommended to simply store the configuration in a properly formatted `.style.yapf` file at the root of your project.

    - You may find pre-configured [.style.yapf](https://github.com/RTBHOUSE/big-bang-py/tree/master/.style.yapf) at the root of this repo.

- It is recommended to include YAPF in your linting Invoke task and also to run it during pre-commit Git hook. Example of both can be found in this repo, see [tasks.py](https://github.com/RTBHOUSE/big-bang-py/tree/master/tasks.py) and [pre-commit](https://github.com/RTBHOUSE/big-bang-py/tree/master/hooks/pre-commit).

- Survival tips:
    
    - If you leave trailing comma in a collection (list, function parameters, etc.), YAPF will force the collection to break, giving one element per line.
    
    - From time to time you WILL see weirdly formatted code, as YAPF is not perfect. There are at least two major occurrences:
 
        - Deeply Nested Dicts - this is quite understandable as decisions that improve readability are usually arbitrary and should be solved on a case-by-case basis.
         
        - Complex Comprehensions - comprehensions are split over multiple lines only when they exceed the column limit... This issue is brought to the attention of both YAPF authors (see issue on [Github](https://github.com/google/yapf/issues/628)) and other programmers (see posts on [Reddit](https://www.reddit.com/r/Python/comments/9mov4r/is_there_a_way_to_force_yapf_to_always_splitfold) and [Stack Overflow](https://stackoverflow.com/questions/52558919/is-there-a-way-to-force-yapf-to-always-split-fold-comprehensions)).
  
    - To manage edge cases, [disable YAPF per line or per block](https://github.com/google/yapf#why-does-yapf-destroy-my-awesome-formatting). 


## Flake8 - Octo-Ninja Linter

- [Flake8](https://github.com/PyCQA/flake8) is a wrapper around three tools:

    1. [PyFlakes](https://github.com/PyCQA/pyflakes) - checks for Python errors.
    
    1. [pycodestyle](https://github.com/PyCQA/pycodestyle) - tests Python code against some of the style conventions in [PEP 8](https://www.python.org/dev/peps/pep-0008/).
    
    1. [McCabe](https://github.com/PyCQA/mccabe) - analyses Python code complexity (see the [next section](#mccabe---code-complexity-checker) for more details).

- Flake8 combines so much linter-power under the hood of a single tool. If used correctly, it will make your code not only more consistent, but simply better (and more pythonic 🐍).

- Flake8 is configurable, where specific setup can be pointed in a [couple of ways](http://flake8.pycqa.org/en/latest/user/configuration.html).

    - You may find pre-configured [.flake8](https://github.com/RTBHOUSE/big-bang-py/tree/master/.flake8) at the root of this repo.

- There is an abundance of [plugins](http://flake8.pycqa.org/en/latest/user/using-plugins.html) greatly extending capability of Flake8 - search for them on GitHub.

    - A bunch of plugins are included in Flake8 configuration of this repo. See all `flake8-*` packages in [Pipfile](https://github.com/RTBHOUSE/big-bang-py/tree/master/Pipfile).
    
    - An interesting example is [flake8-html](https://github.com/lordmauve/flake8-html), which generates readable Flake8 HTML report (similar to `coverage html`).

- It is recommended to include Flake8 in your linting Invoke task and also to run it during pre-commit Git hook. Example of both can be found in this repo, see [tasks.py](https://github.com/RTBHOUSE/big-bang-py/tree/master/tasks.py) and [pre-commit](https://github.com/RTBHOUSE/big-bang-py/tree/master/hooks/pre-commit).


## McCabe - Code Complexity Checker

- [mccabe](https://github.com/pycqa/mccabe) library automatically detects over-complex code basing on cyclomatic complexity.
 
- Cyclomatic complexity is approximately equivalent to one plus the number of loops and if statements. The simple interpretation is that it shows an upper bound for the number of test cases required to obtain branch coverage of the code, therefore it roughly indicates the effort required for writing tests.

    - Additional explanations can be found on [tutorialspoint](https://www.tutorialspoint.com/software_testing_dictionary/cyclomatic_complexity.htm) and [Wikipedia](https://en.wikipedia.org/wiki/Cyclomatic_complexity).

- Code with high cyclomatic complexity (usually assumed as 10+) is likely to be difficult to understand and therefore have a higher probability of containing defects.
    
- It is recommended to include McCabe in your linting Invoke task and also to run it during pre-commit Git hook. In Big-Bang-py McCabe is run automatically by Flake8 linter, see both [tasks.py](https://github.com/RTBHOUSE/big-bang-py/tree/master/tasks.py) and [pre-commit](https://github.com/RTBHOUSE/big-bang-py/tree/master/hooks/pre-commit) at the root of this repo.

    - Cut-off complexity in Invoke task and pre-commit is arbitrarily assumed to be 7 (configured by [max-complexity](http://flake8.pycqa.org/en/latest/user/options.html#cmdoption-flake8-max-complexity) set in [.flake8](https://github.com/RTBHOUSE/big-bang-py/tree/master/.flake8)). However, this number should be adjusted to reflect your experience and project needs.


## Pytest - Test Framework

- **Pytest is programmer-friendly Python test framework. It makes easy to write small tests, yet scales to support complex cases.**

- Major features:

    - Battle-tested and mature.
    
    - Informative test failures.
    
    - Less verbose (plain `assert` vs. `self.assertEqual`, `self.assertGreaterEqual`, etc.)
     
    - Classes are not required.
     
    - A far more convenient way to write setup & teardown functions with fixtures.
     
    - Parameterized tests.
     
    - Fantastic test runner (a.o. marker- and name-based test selection).
    
    - Rich CLI interface.
    
    - Rich plugin architecture.
    
    - Auto-discovery of test modules and functions.
    
    - Can run unittest and nose test suites out of the box.
    
- You can easily set test runner default flags by defining them in a configuration file called `pytest.ini`. You can find [an example](https://github.com/RTBHOUSE/big-bang-py/tree/master/pytest.ini) at the root of this repo.

- Recommended test runner plugins:

    - [pytest-cov](https://pypi.org/project/pytest-cov/) - prints coverage report at the end of test runner report.
    
    - [pytest-mock](https://pypi.org/project/pytest-mock/) - adds `mocker` fixture, which makes mocks easier and more readable.

    - [pytest-socket](https://pypi.org/project/pytest-socket/) - disables socket calls during tests to ensure network calls are prevented. Amazing to protect yourself against incidental DB or API calls.

    - [pytest-sugar](https://pypi.org/project/pytest-sugar/) - makes test runner report even nicer.

- Useful content:

    - [Why pytest?](http://thesoftjaguar.com/pres_pytest.html#/)
    
    - [Official documentation](https://docs.pytest.org/en/latest/contents.html)
    
    - [Python Testing with pytest: Simple, Rapid, Effective, and Scalable](https://www.amazon.com/Python-Testing-pytest-Effective-Scalable/dp/1680502409)
 

## .gitignore

- ALWAYS use `.gitignore`. It specifies files intentionally ignored by Git.

- If you are using PyCharm, definitely install [.ignore plugin](https://github.com/hsz/idea-gitignore). This will make managing `.gitignore` a breeze. 

- Alternatively, it is possible to generate .gitignore online using [gitignore.io](https://www.gitignore.io).

- You may also find an [example](https://github.com/RTBHOUSE/big-bang-py/tree/master/.gitignore) of Python project .gitignore in this repo.


## Pre-commit Git Hook

- The pre-commit Git hook is run before you even start typing new commit message.

- It is a perfect opportunity to automatically run tests and linters, so your code stays consistent and readable, while working as intended.

- You can find an example of pre-commit Git hook in [/hooks/pre-commit](https://github.com/RTBHOUSE/big-bang-py/tree/master/hooks/pre-commit) of this repo.

    - `install_precommit` Invoke task in [tasks.py](https://github.com/RTBHOUSE/big-bang-py/tree/master/tasks.py) takes your pre-commit Git Hook from `/hooks/pre-commit` and automatically sets it up for you.


## Store config in ENVs

- **The [Twelve-Factor App](https://12factor.net/config) stores config in environment variables.**

    - Note that this definition of 'config' does not include internal application config, such as Django or Flask knobs & settings. This type of config does not vary between deploys, nor contains sensitive credentials, so is best done in the code.

- **A litmus test for whether an app has all config correctly factored out of the code is whether the codebase could be made open source at any moment without compromising any secrets or credentials.**

- Usually there are multiple ENV files, like separate versions for testing, development, staging and production. It is recommended to organise those ENVs in one location. 

    - An example of such organisation is present at the root of this repo in [/envs](https://github.com/RTBHOUSE/big-bang-py/tree/master/envs/) folder. You can also find there Python ENVs loader based on [python-dotenv](https://github.com/theskumar/python-dotenv).


## Invoke - Manage & Execute Tasks

- It is recommended to **turn into a task every project related shell command** which will be called more than a couple of times and is not super-common (like `ls` with basic flags).

- **Manage and execute those project tasks via [Invoke](http://www.pyinvoke.org).**

- You can replace `Makefiles` and similar straightaway, as Invoke is dead simple.

- Invoke tasks are called by typing in the shell `invoke *task-name*`

- Invoke tasks are normal Python functions organised in `tasks.py` file.

- Docstrings of functions implementing Invoke tasks are neatly formatted into a command line help:

```
>>> invoke --list
Available tasks:

  task1   First line of task1 docstring.
  task2   First line of task2 docstring.

>>> invoke --help task2
Usage: inv[oke] [--core-opts] task2 [--options] [other tasks here ...]

Docstring:
  Full docstring of task 2.

Options:
  -p TYPE, --param=TYPE   Your additional parameters help string. 
                          See: http://docs.pyinvoke.org/en/0.11.0/getting_started.html#adding-help-for-parameters.
```

- [Invoke tasks can be organised using namespaces](http://docs.pyinvoke.org/en/1.2/getting-started.html#creating-namespaces). Then, for instance, you can call server tasks like `jenkins.deploy`/`jenkins.logs` or organise job-related tasks like `job.start`/`job.stop`.

- Invoke can be easily buffed with [shell tab completion](http://docs.pyinvoke.org/en/1.2/invoke.html#shell-tab-completion).

    - If you work on your projects using `bash` with virtualenv created by `pipenv shell`, a ready-2-go installation script can be found in the file [invoke_bash_completion](https://github.com/RTBHOUSE/big-bang-py/tree/master/invoke_bash_completion) at the root of this repo. If your development environment differs, this script can still give you a basis, or at least a hint, how to build a solution of your own. 

- You may find examples of Invoke tasks in the file [tasks.py](https://github.com/RTBHOUSE/big-bang-py/tree/master/tasks.py) at the root of this repo.

- [The official documentation](http://docs.pyinvoke.org/en/1.2/) is solid. Get familiar with it.


## Logging Is A Programmer's Best Friend

- **You should log. No excuses.**

- Logging makes the flow of the application obvious & visible. This helps every interested party to reason about what and when is happening.

- If done right, logging may literally save your day when real problems shred your beautiful code to pieces in production environment.

- It can be tedious to configure the logging yourself. That is why in [/src/logging_config.py](https://github.com/RTBHOUSE/big-bang-py/tree/master/src/logging_config.py) of this repo you can find pre-configured setup that is ready-to-go.

    - In proposed setup logs are streamed to stderr as well as saved in $PROJECT_ROOT/logs.

    - Logs saved in $PROJECT_ROOT/logs are processed by [RotatingFileHandler](https://docs.python.org/3/library/logging.handlers.html#rotatingfilehandler). Therefore there is no risk that logs will grow indefinitely.

    - How to log:
    
        ```python
        # Load logging config
        import logging.config
        from src.logging_config import DICT_CONFIG
        logging.config.dictConfig(DICT_CONFIG)
        
        # Get logger
        logger = logging.getLogger('main')
        
        # Logging time!
        logger.info('* THE GREAT BIRD IS LISTENING *')
        ```
- `Flake8 + Pipfile` configuration of this repo uses [flake8-print plugin](https://github.com/JBKahn/flake8-print), which will find and warn you about using print statements. If they are no longer necessary, remove them. But if they are... log there! 

- Learn more about logging in a digestible form on [Real Python](https://realpython.com/python-logging/). 

    - If you are an adventurous programmer that knows no fear, there is [official documentation](https://docs.python.org/3/library/logging.html) waiting out there. Bear in mind that because of this document, and its unnecessary complexity, a lot of people were scared off and have been using prints ever since.


## README - Gateway to Your Code

- **Everybody loves good README and so should you. So write it up!**

- README is not only the Golden Gate to open source project. First and foremost, **it is a lantern for the programmers from the future. Most probably, the future you!**

- There is no obvious consensus regarding what README should contain. However, it seems that a good one should answer at least:

    - What is the project about?
        
    - Why is it needed?
        
    - How does it solve the problem?
    
    - How to use the code?
    
    - How to install and test the code?
    
    - How to deploy?
    
    - How to contribute?
    
- If you want to get inspired, [Awesome README](https://github.com/matiassingers/awesome-readme#articles) is a nice place to dig.

- The recommended format of README is [markdown](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet). It is simple, powerful and popular, making it a perfect choice for most of the projects.


## Continuous Integration - Kill Bugs Fast

- Volumes have been written about what is and how to do Continuous Integration (along with Continuous Delivery and Deployment). Yet the absolute minimum every project must implement is to **verify each check-in to a hosted/shared version control by an automated tool in order to detect problems early.**

- **In the short, medium and long-term CI will save you tons of blood & tears. You will also sleep better at night.**

    - Keeping it more serious, CI will take a lot of mental burden off your head. You cannot assume that every contributor has correctly configured pre-commit Git hook. You cannot assume everyone will remember to test and lint. You cannot even trust yourself, because sooner or later you will also make some stupid mistake. That is why you hire CI, to have your project's back.

- There are numerous CI tools, both closely related to your hosting service (like Bitbucket Pipelines or GitLab CI/CD) as well as platform-independent ones (like Jenkins or Circle CI). Choose whatever floats your boat.

- **As to what to check during CI, at least run the tests to double-check they pass.** Some other ideas:

    - Iron the new code with your linters of choice.
    
    - Test if the project still builds correctly.
