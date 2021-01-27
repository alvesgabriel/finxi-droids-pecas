from rest_framework.status import HTTP_200_OK


def test_home(client):
    resp = client.get("/")
    assert resp.status_code == HTTP_200_OK
