install:
	poetry install
build:
	poetry build
package-install:
	python3 -m pip install --user dist/*.whl
lint:
	poetry run flake8 page_loader
test:
	poetry run pytest -vv
test-coverage:
	poetry run pytest --cov=page_loader --cov-report xml
