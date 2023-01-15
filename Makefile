start:
	poetry install
	poetry run sbpars

start-dev:
	poetry run sbpars

install:
	poetry install

check:
	poetry check

lint:
	poetry run flake8