test:
	python georssy/test_georssy.py

compile:
	rm -fr build dist .egg requests.egg-info
	pip install 'twine>=1.5.0'
	python setup.py bdist_wheel --universal

uninstall:
	pip uninstall georssy

local_install:
	pip install dist/georssy-*-py2.py3-none-any.whl

install:
	pip install --no-cache-dir  georssy

publish:
	pip install 'twine>=1.5.0'
	python setup.py bdist_wheel --universal
	twine upload dist/*
	rm -fr build dist .egg requests.egg-info
