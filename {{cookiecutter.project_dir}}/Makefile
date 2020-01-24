RUN_ENVIRONMENT = docker-compose run -e CUSTOM_COMPILE_COMMAND="make requirements" --rm app

include makefiles/clean.mk
include makefiles/docker-compose.mk
include makefiles/docker-repo.mk
include makefiles/help.mk
include makefiles/linters.mk
include makefiles/requirements.mk
include makefiles/tests.mk
