install:
	pip install -r requirements.txt

lint:
	flake8 .

test:
	docker build -f Dockerfile.test -t flask-test .
	docker run --rm -v $(pwd)/reports:/app/reports flask-test

build:
	docker build -t flask-demo .

scan: 
	trivy image flask-demo

smoke:
	docker run -d --rm --name flask-test -p 5000:5000 flask-demo
	sleep 5
	curl --fail http://localhost:5000/
	docker stop flask-test
