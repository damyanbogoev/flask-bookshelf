# Self-Documented Makefile https://marmelab.com/blog/2016/02/29/auto-documented-makefile.html

.PHONY: restore check lint test check help

default: help

restore: ## installs the dependencies based on the requirements file
	@pip install -r requirements.txt

lint: ## runs pylint
	@echo "linting packages and modules ..."
	@pylint bookshelf
	@pylint tests
	@pylint check.py

test: ## runs tests
	@echo "running tests ..."
	@nosetests

check: lint test ## checks the runnable
	@if [ $$? -eq 0 ] ; then echo "NO ISSUES FOUND." ; else echo "ISSUES DETECTED." ; fi

run: ## runs the app
	@echo "starting the application ..."
	@python run.py

help:
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}'