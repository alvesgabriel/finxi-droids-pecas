import pytest
from backend.adverts.models import Advert
from django.urls import reverse
from model_bakery import baker
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_404_NOT_FOUND


@pytest.fixture
def advert_anohter_user(db, address):
    return baker.make(Advert, address=address)


@pytest.fixture
def advert(db, user_advertiser, address):
    return baker.make(Advert, user=user_advertiser, address=address)


@pytest.fixture
def resp_detail_advert(client_logged, advert):
    return client_logged.get(reverse("adverts-detail", kwargs={"pk": advert.id}))


def test_get_advert(client_logged, advert):
    resp = client_logged.get(reverse("adverts-list"))
    assert resp.status_code == HTTP_200_OK


def test_get_advert_not_found(client_logged, advert_anohter_user):
    resp = client_logged.get(reverse("adverts-detail", kwargs={"pk": advert_anohter_user.id}))
    assert resp.status_code == HTTP_404_NOT_FOUND


def test_get_advert_ok(resp_detail_advert):
    assert resp_detail_advert.status_code == HTTP_200_OK


@pytest.mark.parametrize(
    "key",
    (
        "id",
        "user",
        "email",
        "address",
        "description",
        "opened",
    ),
)
def test_keys_advert(resp_detail_advert, key):
    advert_json = resp_detail_advert.json()
    assert key in advert_json.keys()


def test_add_advert(client_logged, advert):
    body = {
        "address": advert.address.id,
        "description": advert.description,
    }
    resp = client_logged.post(reverse("adverts-list"), data=body)
    assert resp.status_code == HTTP_201_CREATED


def test_finalize_advert_status(client_logged, advert):
    resp = client_logged.put(reverse("adverts-finalize", kwargs={"pk": advert.id}))
    assert resp.status_code == HTTP_200_OK


def test_finalize_advert_value(client_logged, advert):
    client_logged.put(reverse("adverts-finalize", kwargs={"pk": advert.id}))
    resp = client_logged.get(reverse("adverts-detail", kwargs={"pk": advert.id}))
    advert_json = resp.json()
    assert not advert_json.get("opened")
