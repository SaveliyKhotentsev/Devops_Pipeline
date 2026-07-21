install:
	pip install -r Flask==3.1.1

lint:
	flake8

test:
	pytest

build:
	docker build -t flask-demo .

