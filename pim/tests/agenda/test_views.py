from http import HTTPStatus


def test_home(client):  # <.>
    response = client.get("/hello-world/")  # <.>
    assert response.status_code == HTTPStatus.OK  # <.>
