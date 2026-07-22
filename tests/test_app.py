import pytest
from app import app as flask_app, tasks

#Fixture — это объект, который pytest создает перед тестом.
#То есть для фйнкций: app эквивалентно flask_app
#Yield — это ключевое слово в Python, которое используется для 
# возврата из функции с сохранением состояния ее локальных
#  переменных, и при повторном вызове такой функции выполнение
#  продолжается с оператора yield, на котором ее работа была прервана
@pytest.fixture
def app():
    return flask_app

#Тестовый клиент Flask.Он позволяет 
# делать запросы без запуска настоящего сервера.
@pytest.fixture
def client(app):
    return app.test_client()

def test_index(app, client):
    response = client.get('/')
    assert response.status_code == 200

def test_version(app, client):
    response = client.get('/version')
    assert response.status_code == 200

def test_health(app, client):
    response = client.get('/health')
    assert response.status_code == 200
    assert response.json['status'] == 'UP'
