all:
	@cat makefile

install:
	pip install -e .

unittest:
	python -m unittest discover -s tests -p 'test_*.py' -b

generate-unittest-docs:
	unittest2doc -s tests -p 'test_*.py'

build-docs:
	make -C sphinx-docs html
clean-docs:
	make -C sphinx-docs clean
	rm -rf sphinx-docs/source/src/*
	rm -rf sphinx-docs/source/unittests/*

build:
	poetry build

# config auth by `poetry config pypi-token.pypi`
publish:
	poetry publish

# config auth by `poetry config pypi-token.testpypi`
test-publish:
	poetry publish --repository testpypi
