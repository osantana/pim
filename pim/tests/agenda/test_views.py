# tag::initial-test-views[]
from http import HTTPStatus


def test_home(client):  # <.>
    response = client.get("/hello-world/")  # <.>
    assert response.status_code == HTTPStatus.OK  # <.>
# end::initial-test-views[]
