import requests
import json

#https://system-service-r0793108.cloud.okteto.net


def test_get_spelers():
    response = requests.get('http://127.0.0.1:8000/spelers')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["spelers"]) == list


def test_get_speler_id():
    response = requests.get('http://127.0.0.1:8000/spelers/{speler_id}')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["db_speler"]) == str


def test_get_teams():
    response = requests.get('http://127.0.0.1:8000/teams')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["teams"]) == list


def test_get_team_id():
    response = requests.get('http://127.0.0.1:8000/teams/{team_id}')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["db_team"]) == str


def test_get_users():
    response = requests.get('http://127.0.0.1:8000/users')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["users"]) == list


def test_get_user_id():
    response = requests.get('http://127.0.0.1:8000/users/{user_id}')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["db_user"]) == str


def test_get_user_me():
    response = requests.get('http://127.0.0.1:8000/users/me')
    assert response.status_code == 200
    response_dictionary = json.loads(response.text)
    assert type(response_dictionary["current_user"]) == str
