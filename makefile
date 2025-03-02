all:
	@cat makefile

install:
	pip install .
dev-install:
	pip install -e .[dev]

unittest:
	python -m unittest discover -s tests -p 'test_*.py' -b

generate-unittest-docs:
	unittest2doc -s tests -p 'test_*.py'

build-docs:
	make -C sphinx-docs html
