## TL;DR

- Use [.gitignore](https://git-scm.com/docs/gitignore).

- Use Python 3.7.

- Manage your dependencies using [Pipenv](https://pipenv.readthedocs.io/en/latest).

- Manage and execute your command line tasks via [Invoke](http://www.pyinvoke.org).


## .gitignore

- ALWAYS use `.gitignore`. It specifies files intentionally ignored by Git.

- If you are using PyCharm, definitely install [.ignore plugin](https://github.com/hsz/idea-gitignore). This will make managing `.gitignore` a breeze. 

- Alternatively, it is possible to generate .gitignore online using [gitignore.io](https://www.gitignore.io).

- You may also find [example](https://bitbucket.org/rtbhouse/big-bang-py/src/master/.gitignore) of Python project .gitignore in this repo.

    - Task `update_gitignore` in [tasks.py](https://bitbucket.org/rtbhouse/big-bang-py/src/master/tasks.py) automates updating .gitignore in your repo by copying the version from local copy of Big-Bang-py.


## Python version

- **It is recommended to use Python 3.7.**

- There is a nice summary of new features on [Real Python](https://realpython.com/python37-new-features). More detailed description can be found in [official docs](https://docs.python.org/3/whatsnew/3.7.html).

- To name some notable additions:

    - [Data Classes](https://realpython.com/python-data-classes) can easily replace [namedtuples](https://docs.python.org/3.7/library/collections.html#collections.namedtuple) and [attrs](https://github.com/python-attrs/attrs).
    
    - [Typing Forward Reference](https://realpython.com/python37-new-features/#typing-enhancements) makes type hints even more programmer-friendly.

    - The `asyncio` module has received many [new features, usability and performance improvements](https://docs.python.org/3/whatsnew/3.7.html#asyncio). For instance,  new `asyncio.run()` function can be used to run a coroutine from synchronous code by automatically creating and destroying the event loop.
    
- If for some reason you are still using previous versions of Python (especially version 3.6), it is possible to backport some features e.g. [Data Classes](https://github.com/ericvsmith/dataclasses).


## Pipenv - Python Packing Tool

- **Use [Pipenv](https://pipenv.readthedocs.io/en/latest) as Python packaging tool.**

- Pipenv consolidates `pip` & `virtualenv` as well as offers some powerful features:

    - Pipenv automatically creates and manages a virtualenv.
    
    - You specify the project packages in `Pipfile`. Because those are abstract dependency declarations, **you declare only the packages you need**.
    
    -  `Pipfile.lock` holds locked/hashed combination of all dependencies (including sub-dependencies) of your project. This ensures repeatable, deterministic builds. You never manage this file by hand, as Pipenv takes care of it.
    
    - Essential commands:
    
        - `shell`: spawns a shell with the virtualenv activated. If a `.env` file is present in your project, shell will automatically load it for you.
        
        - `run`: runs a given command from the virtualenv, with any arguments forwarded (e.g. `$ pipenv run python`).
        
        - `graph`: shows a dependency graph of installed dependencies.
        
        - `check`: **checks for security vulnerabilities** and asserts that PEP 508 requirements are being met by the current environment.

- You can educate yourself further by reading a [Real Python's guide](https://realpython.com/pipenv-guide). It is also recommended to go through [the official documentation](https://pipenv.readthedocs.io/en/latest/).


## Invoke - Task Management & Command Execution

- It is recommended to **turn into a task every project related shell command** which will be called more than a couple of times and is not super-common (like `ls` with basic flags).

- **Manage and execute those project tasks via [Invoke](http://www.pyinvoke.org).**

- You can easily replace `Makefiles` and similar tools as Invoke is dead simple.

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

- You may find examples of tasks in `tasks.py` in project root of this repo.

- [The official documentation](http://docs.pyinvoke.org/en/1.2/) is solid, so it is recommended get familiar with it. 
