from main import app
import pytest
from flask import request

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

def test_helloWorld(client):
    response = client.get('/helloWorld')
    assert response.status_code == 200
    assert response.data.decode() == 'Hello world!'

@pytest.mark.parametrize("name, expected_output", [
    (None, "Hello world!"),
    ("", "Hello world!"),
    ("John", "Hello John!")
])
def test_hello_world_parameters(client, name, expected_output):
    response = client.get('/helloWorldParameters', query_string={'name': name})
    assert response.status_code == 200
    assert response.data.decode() == expected_output
