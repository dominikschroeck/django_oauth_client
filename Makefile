test:
	pytest --workers auto tests --no-coverage-upload

test-with-typeguard:
	pytest --workers auto --typeguard-packages=django_oauth_client tests --no-coverage-upload

coverage:
	pytest --workers auto --cov-config=.coveragerc --cov=django_oauth_client --cov-report=term-missing --cov-report=xml --junitxml=junit/test-results.xml tests

mypy:
	mypy -p django_oauth_client --exclude "snowflake|csv_to_pandera_schema|progressbar|pandas"

bandit:
	bandit -r django_oauth_client -r -c .bandit

flake8:
	flake8 --config .flake8 django_oauth_client

pylint:
	pylint --fail-under=8 django_oauth_client

safety:
	pip-audit

build:
	python setup.py bdist_wheel sdist

publish:
	python3 -m twine upload dist/*