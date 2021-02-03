import pytest
from django.urls import reverse
from rest_framework.status import HTTP_200_OK


@pytest.fixture
def resp_login(client, user_advertiser):
    login = {
        "username": user_advertiser.email,
        "password": user_advertiser.flat_password,
    }
    return client.post(reverse("login-token"), data=login)


def test_login_status(resp_login):
    assert resp_login.status_code == HTTP_200_OK


def test_login_token(resp_login):
    login_json = resp_login.json()
    assert "token" in login_json
