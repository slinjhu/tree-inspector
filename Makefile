.PHONY: dist test dist clean

PIP=env/bin/pip
PY=env/bin/python


env:
	rm -rf env
	python3.7 -m venv env
	${PIP} install -U pip setuptools wheel
	${PIP} install -e .
	${PIP} install twine uuid

dist: env
	rm -rf build dist || true
	${PY} setup.py sdist bdist_wheel

upload-test: dist
	./env/bin/twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	echo "View at: https://test.pypi.org/project/tree-inspector"

upload-prod: clean test dist
	./env/bin/twine upload dist/*

test: env
	${PY} -m unittest discover ./tests/

clean:
	(rm -rf env dist build)