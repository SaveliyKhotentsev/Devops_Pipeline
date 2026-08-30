install:
	python3 -m venv venv
	venv/bin/python -m pip install --upgrade pip
	venv/bin/python -m pip install -r requirements.txt
	venv/bin/python -m pip install -e .

up:
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	mkdir -p reports
	venv/bin/python -m flake8 app.py > reports/flake8-report.txt || true

test:
	mkdir -p reports
	venv/bin/python -m pytest --junitxml=reports/junit-report.xml

unit_test:
	mkdir -p reports
	venv/bin/python -m pytest -m "unit" --junitxml=reports/junit-report.xml

integration_test:
	mkdir -p reports
	venv/bin/python -m pytest -m "integration" --junitxml=reports/junit-report.xml

build:
	id
	docker build -t flask-demo:1.1.0 .

doc-com:
	id
	docker compose build
	pwd
	ls -la
	file init.sql
	docker compose up 

scan:
	mkdir -p reports
	trivy image \
		--format table \
		-o reports/trivy-report.txt \
		flask-demo

smoke:
	docker run -d --rm --name flask-test --network=jenkins -p 5000:5000 flask-demo
	sleep 5
	docker ps -a
	docker logs flask-test
	IP=$$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' flask-test); \
	echo $$IP; \
	curl --fail http://$$IP:5000/;

smoke2:
	docker compose up --build
	sleep 5
	docker ps -a
	docker logs flask-test
	IP=$$(docker inspect -f '{{range.NetworkSettings.Networks}}{{.IPAddress}}{{end}}' flask-test); \
	echo $$IP; \
	curl --fail http://$$IP:5000/;

stop:
	docker stop flask-test

stop_compose:
	docker compose down -v 
