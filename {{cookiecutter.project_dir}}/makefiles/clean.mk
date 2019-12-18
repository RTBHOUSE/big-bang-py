.PHONY: clean
clean: clean-pyc clean-test ## removes all test, coverage and Python artifacts

.PHONY: clean-pyc
clean-pyc: ## removes Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

.PHONY: clean-test
clean-test: ## removes test and coverage artifacts
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache/
	rm -fr .mypy_cache/
