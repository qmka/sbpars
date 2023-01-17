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

build:
	poetry build

publish-dev:
	poetry publish --dry-run
	python3 -m pip install --user dist/*.whl