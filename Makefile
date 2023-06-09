install:
	poetry install
package-install:
	python3 -m pip install --user dist/*.whl
force-reinstall:
	python3 -m pip install --force-reinstall dist/*.whl
build:
	poetry build
publish:
	poetry publish --dry-run
lint:
	poetry run flake8 gendiff
test:
	python3 tests/test.py
test-coverage:
	poetry run pytest
