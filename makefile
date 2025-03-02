all:
	@cat makefile

update-docs:
	rsync -a ./sphinx-docs/build/html/ docs/
	touch docs/.nojekyll
