.PHONY: deps test

deps:
		pip install -r requirements.txt
		pip install -r test_requirements.txt
		
test:
    python -m unittest discover -p '*tests.py' -v