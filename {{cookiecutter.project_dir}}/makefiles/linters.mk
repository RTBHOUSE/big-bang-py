.PHONY: linters
linters: black flake8 mypy isort bandit ## checks code style

.PHONY: flake8
flake8: ## checks codebase with flake8
	$(RUN_ENVIRONMENT) flake8 src tests

.PHONY: mypy
mypy: ## checks typehints
	$(RUN_ENVIRONMENT) mypy src tests

.PHONY: isort
isort: ## checks if imports are sorted correctly
	$(RUN_ENVIRONMENT) isort -rc -c src tests

.PHONY: isort_fix
isort_fix: ## fixes imports
	$(RUN_ENVIRONMENT) isort -rc src tests

.PHONY: bandit
bandit: ## checks if there aren't any secrets in code
	$(RUN_ENVIRONMENT) bandit -r src

.PHONY: black
black: ## check codebase with black
	$(RUN_ENVIRONMENT) black --check --diff --line-length 100 .

.PHONY: black_fix
black_fix: ## fixes code style
	$(RUN_ENVIRONMENT) black --line-length 100 src tests
