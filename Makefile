.PHONY: env

PIP=env/bin/pip
PY=env/bin/python


env:
	rm -rf env
	python3.7 -m venv env
	${PIP} install -U pip setuptools wheel
	${PIP} install -r requirements.txt