.PHONY: venv test
BIN=venv/bin/

venv: requirements.txt
	test -d venv || virtualenv venv
	venv/bin/pip install -qUr requirements.txt
	touch venv/bin/activate

test: venv
	$(BIN)python3 -m unittest discover -s tests -v