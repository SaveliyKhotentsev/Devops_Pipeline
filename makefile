install:
	python3 -m venv venv
	venv/bin/python -m pip install --upgrade pip
	venv/bin/python -m pip install -r requirements.txt

up:
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	mkdir -p reports
	venv/bin/python -m flake8 app.py > reports/flake8-report.txt || true

test:
	venv/bin/python -m pytest --junitxml=reports/junit-report.xml

build:
	id
	docker build -t flask-demo .

scan: 
	trivy image flask-demo

smoke:
	docker run -d --rm --name flask-test -p 5000:5000 flask-demo
	sleep 5
	docker ps -a
	docker logs flask-test
	curl --fail http://localhost:5000/
	docker stop flask-test
