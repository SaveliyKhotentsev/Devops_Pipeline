install:
	python3 -m venv venv
	venv/bin/python -m pip install --upgrade pip
	venv/bin/python -m pip install -r requirements.txt

lint:
	venv/bin/python -m flake8 .

test:
	venv/bin/python -m pytest --junitxml=reports/junit-report.xml

build:
	venv/bin/python -m docker build -t flask-demo .

scan: 
	venv/bin/python -m trivy image flask-demo

smoke:
	venv/bin/python -m docker run -d --rm --name flask-test -p 5000:5000 flask-demo
	venv/bin/python -m sleep 5
	venv/bin/python -m curl --fail http://localhost:5000/
	venv/bin/python -m docker stop flask-test
