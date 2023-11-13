.PHONY: install
install:
	pip3 install poetry
	poetry install

.PHONY: run-local
run-local:
	poetry run python3 src/main.py

.PHONY: build
build:
	docker build -t devdays2023img .
