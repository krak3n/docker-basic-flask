#
# Generic functions
#

clean_pyc:
	find . -name \*.pyc -delete

documentation:
	make -C docs clean
	make -C docs html

#
# Install for development
#

# Install Development Requirements
install_develop:
	./install.sh develop

develop: install_develop

#
# Install for test running
#

# Install Test Requirements
install_test:
	./install.sh test

# Test Command
run_tests:
	python setup.py test

test: install_test run_tests

#
# Application Related Commands
#

runserver:
	python src/foo/run.py
