.PHONY: dist

PIP=env/bin/pip
PY=env/bin/python


env:
	rm -rf env
	python3.7 -m venv env
	${PIP} install -U pip setuptools wheel
	${PIP} install -e .
	${PIP} install twine

dist: env
	rm -rf build dist || true
	${PY} setup.py sdist bdist_wheel

upload-test:
	./env/bin/twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	echo "View at: https://test.pypi.org/project/tree-inspector"

upload-prod:
	./env/bin/twine upload dist/*