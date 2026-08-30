import pytest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from app import app as flask_app

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


@pytest.mark.integration
def test_post():
    response = client.post(
        "/users",
        json={
            "id": "3",
            "name": "Bob",
            "email": "Bob@email"
        }
    )
    assert response.status_code == 200


@pytest.mark.integration
def test_false_post():
    response = client.post(
        "/users",
        json={
            "abra": "kadabra",
            "abra": "kadabra",
            "abra": "kadabra",
            "abra": "kadabra",
            "abra": "kadabra"
        }
    )
    assert response.status_code == 400

    
@pytest.mark.integration
def test_get():
    response = client.get("/users/3")
    assert response.status_code == 200
    assert response.name == "BOB"
    assert response.email == "Bob@email"


@pytest.mark.integration
def test_false_get():
    response = client.get("/users/228")
    assert response.status_code == 40



