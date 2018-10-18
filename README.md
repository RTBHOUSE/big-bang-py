## TL;DR Checklist

- Python:

    - Use [Python 3.7](https://docs.python.org/3/whatsnew/3.7.html).
    
    - Manage dependencies using [Pipenv](https://pipenv.readthedocs.io/en/latest).
    
    - Format source files with [YAPF](https://github.com/google/yapf).
    
    - Sort imports with [Isort](https://github.com/timothycrosley/isort).
    
    - Scan code complexity by calling `run-mccabe.py`.
    
    - Use [pytest](https://docs.pytest.org/en/latest/) as test framework.

- Git:

    - Use [.gitignore](https://git-scm.com/docs/gitignore).
    
    - Use [pre-commit Git hook](https://bitbucket.org/rtbhouse/big-bang-py/src/master/hooks/pre-commit).

- Project:

    - Store config (credentials, secrets, etc.) in [ENVs](https://12factor.net/config).
    
    - Manage and execute command line tasks via [Invoke](http://www.pyinvoke.org).


## Initialization & Update

- To initialize Big-Bang-py in your project, run [start_big_bang.py](https://bitbucket.org/rtbhouse/big-bang-py/src/master/start_big_bang.py) script in the target directory.

    - Prerequisites:
        
        - Pipenv.
    
        - `BIG_BANG_PY_DIR` ENV holding full path to the local copy of Big-Bang-py.
        

- If you wish to simply update Big-Bang-py files, adjust & run task `update_big_bang_files` in [tasks.py](https://bitbucket.org/rtbhouse/big-bang-py/src/master/tasks.py).
    

## Python version

- **It is recommended to use Python 3.7.**

- There is a nice summary of new features on [Real Python](https://realpython.com/python37-new-features). More detailed description can be found in [official docs](https://docs.python.org/3/whatsnew/3.7.html).

- To name some notable additions:

    - [Data Classes](https://realpython.com/python-data-classes) can easily replace [namedtuples](https://docs.python.org/3.7/library/collections.html#collections.namedtuple) and [attrs](https://github.com/python-attrs/attrs).
    
    - [Typing Forward Reference](https://realpython.com/python37-new-features/#typing-enhancements) makes type hints even more programmer-friendly.

    - The `asyncio` module has received many [new features, usability and performance improvements](https://docs.python.org/3/whatsnew/3.7.html#asyncio). For instance,  new `asyncio.run()` runs coroutine in automatically created and destroyed event loop.
    
- If for some reason you use previous version of Python (especially 3.6), it is possible to backport some of the new features e.g. [Data Classes](https://github.com/ericvsmith/dataclasses).


## Pipenv - Python Package Manager

- **[Pipenv](https://pipenv.readthedocs.io/en/latest) consolidates `pip` & `virtualenv` while offering powerful features. Use it to manage Python dependencies.** 

- Pipenv automatically creates and manages virtual environment.

- You specify project packages in `Pipfile`. Because those are abstract dependency declarations, **you declare only the packages you need**. Sub-dependencies are taken care of by Pipenv.

-  `Pipfile.lock` uses hashes to lock all of the dependencies (i.e. including sub-dependencies). This ensures repeatable, deterministic builds. You never manage this file by hand, leaving the matter for Pipenv.

- You install project dependencies using `Pipfile` (building from the latest allowed versions of packages) or `Pipfile.lock` (making build deterministic).

    - **Pipfile with the packages necessary to run all the content of Big-Bang-py may be found in this repo's [Pipfile](https://bitbucket.org/rtbhouse/big-bang-py/src/master/Pipfile).**
    
- Essential commands:

    - **`shell` - spawns a shell with the virtualenv activated. If `.env` file is present in your project root, shell will automatically load it for you.**
    
    - `run`: runs a given command from the virtualenv, with any arguments forwarded (e.g. `$ pipenv run python`). If `.env` file is present in your project root, shell will automatically load it for you.
    
    - `graph`: shows a dependency graph of the installed dependencies.
    
    - `check`: **checks for security vulnerabilities** and asserts that PEP 508 requirements are being met by the current environment.

- You can educate yourself further by reading a [Real Python's guide](https://realpython.com/pipenv-guide). It is also recommended to go through [the official documentation](https://pipenv.readthedocs.io/en/latest/).


## YAPF - Python Files Formatter

- **[YAPF](https://github.com/google/yapf) is a Python files formatter with the ultimate goal of producing code as good as the code that a programmer would write if they were following a style guide.**

- The formatting style used by YAPF is configurable. Specific configuration can be pointed in a couple of ways. However, it is recommended to simply store it in a properly formatted `.style.yapf` file in the root of your project, so YAPF can automatically pick this config up.

- You may find pre-configured [.style.yapf](https://bitbucket.org/rtbhouse/big-bang-py/src/master/.style.yapf) in the root of this repo.

- It is recommended to include YAPF in your linting Invoke task and also to run it during pre-commit Git hook. Example of both can be found in [tasks.py](https://bitbucket.org/rtbhouse/big-bang-py/src/master/tasks.py) and [pre-commit](https://bitbucket.org/rtbhouse/big-bang-py/src/master/hooks/pre-commit) in the root of this repo.

- Survival tips:
    
    - If you leave trailing comma in a collection (list, function parameters, etc.) YAPF will force the collection to break giving one element per line.
    
    - From time to time you WILL see weirdly formatted code as YAPF is not perfect. There are at least two major occurrences:
 
        - Deeply Nested Dicts - this is quite understandable as decisions that improve readability are usually arbitrary and should be solved on a case-by-case basis.
         
        - Complex Comprehensions - YAPF assumes that only comprehension that exceed column limit are complex enough to be formatted... This issue is brought to the attention of both YAPF authors (see issue on [Github](https://github.com/google/yapf/issues/628)) and other programmers (see posts on [Stack Overflow](https://stackoverflow.com/questions/52558919/is-there-a-way-to-force-yapf-to-always-split-fold-comprehensions) and [Reddit](https://www.reddit.com/r/Python/comments/9mov4r/is_there_a_way_to_force_yapf_to_always_splitfold)).
  
    - To manage edge cases, [disable YAPF per line or per block](https://github.com/google/yapf#why-does-yapf-destroy-my-awesome-formatting). 
    

## Isort - Python Imports Sorter

- **[Isort](https://github.com/timothycrosley/isort) sorts Python imports alphabetically and separates them into defined sections.**

- There are several ways to configure Isort's behavior. Full reference of every setting can be found [here](https://github.com/timothycrosley/isort/wiki/isort-Settings#full-reference-of-isort-settings).

- You can specify project level configuration simply by placing a `.isort.cfg` file at the root of your project.

- You may find pre-configured [.isort.cfg](https://bitbucket.org/rtbhouse/big-bang-py/src/master/.isort.cfg) in the root of this repo.
    
- It is recommended to include Isort in your linting Invoke task and also to run it during pre-commit Git hook. Example of both can be found in [tasks.py](https://bitbucket.org/rtbhouse/big-bang-py/src/master/tasks.py) and [pre-commit](https://bitbucket.org/rtbhouse/big-bang-py/src/master/hooks/pre-commit) in the root of this repo.

- To manage edge cases, [disable Isort per line or for entire file](https://github.com/timothycrosley/isort#skip-processing-of-imports-outside-of-configuration).


## McCabe - Code Complexity Checker

- [mccabe](https://github.com/pycqa/mccabe) library automatically detects over-complex code based on cyclomatic complexity (for curious, consult [tutorialspoint](https://www.tutorialspoint.com/software_testing_dictionary/cyclomatic_complexity.htm) and [Wikipedia](https://en.wikipedia.org/wiki/Cyclomatic_complexity)).

- Cyclomatic complexity is roughly equivalent to one plus the number of loops and if statements. The simple interpretation is that it is an upper bound for the number of test cases required to obtain branch coverage of the code. So, in the context of testing, cyclomatic complexity can be used to estimate the required effort for writing tests.

- Code with high cyclomatic complexity (usually assumed as 10+) is likely to be difficult to understand and therefore have a higher probability of containing defects.
    
- It is recommended to include McCabe in your linting Invoke task and also to run it during pre-commit Git hook. Example of both can be found in [tasks.py](https://bitbucket.org/rtbhouse/big-bang-py/src/master/tasks.py) and [pre-commit](https://bitbucket.org/rtbhouse/big-bang-py/src/master/hooks/pre-commit) in the root of this repo.

    - Cut-off complexity is currently assumed to be 7. However, this number should be adjusted to reflect your experience and project needs.


## Pytest - Python Test Framework

- **Pytest is the recommended Python test framework.**

    - It is simple & programmer-friendly.
    
    - Offers great depth and complexity, but only if necessary.

- Major features:

    - Battle-tested and mature.
    
    - Informative test failures.
    
    - Less verbose (assert vs. self.assertEqual etc.).
     
    - Classes are not required.
     
    - A far more convenient way to write setup/teardown functions with fixtures.
     
    - Parameterized tests.
     
    - Nice test runner (marker- and name-based test selection).
    
    - Rich CLI interface.
    
    - Rich plugin architecture.
    
    - Auto-discovery of test modules and functions.
    
    - Can run unittest and nose test suites out of the box.
    
- You can easily change command line options defaults by defining them in a configuration file called `pytest.ini`. You can find [an example](https://bitbucket.org/rtbhouse/big-bang-py/src/master/pytest.ini) in the root of this repo.

- Recommended plugins:

    - [pytest-cov](https://pypi.org/project/pytest-cov/) - prints coverage report at the end of test runner report.
    
    - [pytest-mock](https://pypi.org/project/pytest-mock/) - adds `mocker` fixture, which makes mocks easier and more readable.

    - [pytest-socket](https://pypi.org/project/pytest-socket/) - disables socket calls during tests to ensure network calls are prevented. Amazing to protect yourself against incidental DB or API calls.

    - [pytest-sugar](https://pypi.org/project/pytest-sugar/) - makes test runner report even nicer.

- Useful content:

    - [Why pytest?](http://thesoftjaguar.com/pres_pytest.html#/)
    
    - [Official documentation](https://docs.pytest.org/en/latest/contents.html)
    
    - [Python Testing with pytest: Simple, Rapid, Effective, and Scalable](https://www.amazon.com/Python-Testing-pytest-Effective-Scalable/dp/1680502409)
    

## Store config in ENVs

- **The [Twelve-Factor App](https://12factor.net/config) stores config in environment variables.**

    - Note that this definition of 'config' does not include internal application config, such as Django or Flask knobs & settings. This type of config does not vary between deploys, nor contains sensitive credentials, so is best done in the code.

- **A litmus test for whether an app has all config correctly factored out of the code is whether the codebase could be made open source at any moment without compromising any secrets or credentials.**

- Usually there are multiple ENV files e.g. separate versions for testing, devel, staging and production. It is recommended to organise those ENVs in one location. 

    - An example is present in the root of this repo in [/envs](https://bitbucket.org/rtbhouse/big-bang-py/src/master/envs/) folder. 
    
    - You can also find there ENVs loader based on [python-dotenv](https://github.com/theskumar/python-dotenv).


## Invoke - Task Management & Command Execution

- It is recommended to **turn into a task every project related shell command** which will be called more than a couple of times and is not super-common (like `ls` with basic flags).

- **Manage and execute those project tasks via [Invoke](http://www.pyinvoke.org).**

- You can replace `Makefiles` and similar straightaway, as Invoke is dead simple.

- Invoke tasks are called by typing in the shell `invoke *task-name*`

- Invoke tasks are normal Python functions organised in `tasks.py` file.

- Docstrings of Invoke tasks functions are neatly converted into classic command line tool help:

```
>>> invoke --list
Available tasks:

  task1      First line of docstring of task1.
  task2      First line of docstring of task2.

# Get full docstring of a particular task:  
>>> invoke --help *task-name*
```

- [Invoke tasks can be organised using namespaces](http://docs.pyinvoke.org/en/1.2/getting-started.html#creating-namespaces). Then, for instance, you can call server tasks like `jenkins.deploy`/`jenkins.logs` or organise job-related tasks like `job.start`/`job.stop`.

- You may find examples of tasks in this repo's [tasks.py](https://bitbucket.org/rtbhouse/big-bang-py/src/master/tasks.py).

- [The official documentation](http://docs.pyinvoke.org/en/1.2/) is solid, so it is recommended to get familiar with it. 


## .gitignore

- ALWAYS use `.gitignore`. It specifies files intentionally ignored by Git.

- If you are using PyCharm, definitely install [.ignore plugin](https://github.com/hsz/idea-gitignore). This will make managing `.gitignore` a breeze. 

- Alternatively, it is possible to generate .gitignore online using [gitignore.io](https://www.gitignore.io).

- You may also find [example](https://bitbucket.org/rtbhouse/big-bang-py/src/master/.gitignore) of Python project .gitignore in this repo.


## Pre-commit Git Hook

- The pre-commit Git hook is run before you even type in a commit message.

- It is a perfect opportunity to automatically run tests and linters, so your code is consistent, readable and works as intended.

- You can find an example of pre-commit Git hook in [/hooks/pre-commit](https://bitbucket.org/rtbhouse/big-bang-py/src/master/hooks/pre-commit) of this repo.

    - `install_precommit` Invoke task in [tasks.py](https://bitbucket.org/rtbhouse/big-bang-py/src/master/tasks.py)  takes your pre-commit Git Hook from `/hooks/pre-commit` and sets it up for you.
