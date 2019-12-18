.PHONY: requirements
requirements: ## compiles all the requirements files
	$(RUN_ENVIRONMENT) pip-compile --generate-hashes -o requirements/requirements.txt requirements/requirements.in

.PHONY: update_requirements
update_requirements: ## updates all the requirements
	$(RUN_ENVIRONMENT) pip-compile --upgrade --generate-hashes -o requirements/requirements.txt requirements/requirements.in
