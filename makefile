install:
	pip install -r requirements.txt

lint:
	flake8 .

test:
	pytest --junitxml=reports/junit-report.xml

build:
	docker build -t flask-demo .

scan: 
	trivy image flask-demo

smoke:
	docker run -d --rm --name flask-test -p 5000:5000 flask-demo
	sleep 5
	curl --fail http://localhost:5000/
	docker stop flask-test
