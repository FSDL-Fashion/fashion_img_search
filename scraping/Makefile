POETRY := $(shell command -v poetry 2> /dev/null)

.DEFAULT_GOAL := help

.PHONY: install
install:  ## Install the dependencies and headless chromium for web scraping
	@if [ -z $(POETRY) ]; then echo "Poetry could not be found. See https://python-poetry.org/docs/"; exit 2; fi
	@$(POETRY) install --with scraping
	@echo "Installing chromium"
	@playwright install chromium
	@export NODE_OPTIONS="--max-old-space-size=8192"  # increase heap size to avoid https://github.com/scrapy-plugins/scrapy-playwright/issues/19
	@if [ -z "${AWS_ACCESS_KEY_ID}" ]; then echo "Add your AWS credentials to the environment."; fi

.PHONY: scraping
scraping:  ## Launch scraping script
	@$(POETRY) run python -m scraping.engine

.PHONY: help
help:  ## Show this help message
	@echo
	@echo "usage: make [target]"
	@echo
	@echo "targets:"
	@awk -F ':|##' '/^[^\t].+?:.*?##/ {printf "\033[36m%-30s\033[0m %s\n", $$1, $$NF}' Makefile
	@echo
