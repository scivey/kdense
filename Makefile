test:
	nosetests kdense/test

lint:
	pyflakes kdense

publish:
	python setup.py register -r pypi && python setup.py sdist upload -r pypi

.PHONY: test publish lint
