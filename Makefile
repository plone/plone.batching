# Generated from:
# https://github.com/plone/meta/tree/master/config/default
MAKEFLAGS += --no-print-directory # supress output that directory is changed

PY_FILES = find plone -name "*.py"
RST_FILES = find plone -name "*.rst"

.PHONY: help ## Print this help
help:
	@grep -E '^\.PHONY: [0-9a-zA-Z_-]+ .*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = "(: |##)"}; {printf "\033[1m%-30s\033[0m %s\n", $$2, $$3}'

.PHONY: format ## Format python code with pyupgrade/isort/black
format:
	pyupgrade --py38-plus *.py `$(PY_FILES)` && \
	isort *.py `$(PY_FILES)` && \
	black *.py `$(PY_FILES)`

.PHONY: qa ## Check code for typos and code smells
qa:
	codespell *.rst `$(RST_FILES)` *.py `$(PY_FILES)` && \
	flake8 *.py `$(PY_FILES)`
