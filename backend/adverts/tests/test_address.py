import pytest
from backend.adverts.models import Address
from django.urls import reverse
from model_bakery import baker
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND


@pytest.fixture
def address_not_user(db):
    return baker.make(Address)


@pytest.fixture
def resp_lit_address(client_logged, address):
    return client_logged.get(reverse("addresses-list"))


@pytest.fixture
def resp_detail_address(client_logged, address):
    return client_logged.get(reverse("addresses-detail", kwargs={"pk": address.id}))


@pytest.fixture
def address_keys():
    return "id user zip_code street district city state".split()


def test_status_address(resp_lit_address):
    assert resp_lit_address.status_code == HTTP_200_OK


def test_total_address(resp_lit_address):
    address_json = resp_lit_address.json()
    assert address_json.get("count") == 1


def test_get_address_not_fount(client_logged, address_not_user):
    resp = client_logged.get(reverse("addresses-detail", kwargs={"pk": address_not_user.id}))
    assert resp.status_code == HTTP_404_NOT_FOUND


def test_get_address_ok(resp_detail_address):
    assert resp_detail_address.status_code == HTTP_200_OK


@pytest.mark.parametrize(
    "key",
    ("id", "zip_code", "street", "district", "city", "uf"),
)
def test_keys_address(resp_detail_address, key):
    address_json = resp_detail_address.json()
    assert key in address_json.keys()


def test_add_address(client_logged, address):
    body = {
        "zip_code": address.zip_code,
        "street": address.street,
        "district": address.district,
        "city": address.city,
        "uf": address.uf,
        "number": address.number,
    }
    resp = client_logged.post(reverse("addresses-list"), data=body)
    assert resp.status_code == HTTP_201_CREATED
