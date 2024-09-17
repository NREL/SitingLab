.PHONY: help book clean serve

help:
	@echo "Please use 'make <target>' where <target> is one of:"
	@echo "  clean       to clean out site build files"
	@echo "  install     to install the necessary dependencies for jupyter-book to build"
	@echo "  book        to convert the content/ folder into Jekyll markdown in _build/"
	@echo "  runall      to run all notebooks in-place, capturing outputs with the notebook"

clean:
	rm -rf _build

install:
	jupyter-book install ./

book: clean
	jupyter-book build ./

runall:
	jupyter-book run ./notebooks
