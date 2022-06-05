import requests

BASE_URL = 'http://127.0.0.1:5000'
user = {'email': 'user3@test.com', 'password': 'P@ssw0rd'}


def test_home_page_check_status_code_equals_200():
    response = requests.get(f"{BASE_URL}")
    assert response.status_code == 200


def test_login_page_check_status_code_equals_200():
    response = requests.get(f"{BASE_URL}/login")
    assert response.status_code == 200


def test_login_check_status_code_equals_200():
    response = requests.post(f"{BASE_URL}/login", data=user)
    assert response.status_code == 200


def test_profile_page_check_status_code_equals_200():
    response = requests.get(f"{BASE_URL}/profile")
    assert response.status_code == 200


def test_logout_check_status_code_equals_200():
    response = requests.get(f"{BASE_URL}/logout")
    assert response.status_code == 200
