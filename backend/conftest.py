import pytest
from model_bakery import baker

from backend.adverts.models import Address


@pytest.fixture
def user_advertiser(db, django_user_model):
    password = "May the Force be with you!"
    user = baker.make(
        django_user_model, first_name="Watto", email="watto@tatooine.com", password=password, is_advertiser=True
    )
    user.flat_password = password
    return user


@pytest.fixture
def client_logged(client, user_advertiser):
    client.force_login(user_advertiser)
    return client


@pytest.fixture
def address(db, user_advertiser):
    return baker.make(Address, user=user_advertiser)
