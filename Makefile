# Makefile
# vim:ft=make

all: install

install:
	python setup.py install

install.hack:
	pip install -r requirements.txt
	pip install -r dev-requirements.txt

lint:
	pylint --reports no agile tests

# TODO lint !
test: warn_missing_linters
	py.test --verbose --cov=agile tests/

present_pylint=$(shell which pylint)
present_pytest=$(shell which py.test)
warn_missing_linters:
	@test -n "$(present_pylint)" || echo "WARNING: pylint not installed."
	@test -n "$(present_pytest)" || echo "WARNING: py.test not installed."

coverage: test
ifndef CODECOV_TOKEN
	$(error codecov token not defined)
endif
	codecov --token=$(CODECOV_TOKEN)

.PHONY: clean
clean:
	rm -rf *.egg-info dist build
	find . -name '__pycache__' -exec rm -f {} +
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
