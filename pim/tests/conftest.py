import pytest


@pytest.fixture
def default_user_data():
    return {
        "username": "john",
        "password": "sekret",
        "email": "john.doe@example.com",
    }


@pytest.fixture
def default_user(django_user_model, default_user_data):  # <.>
    return django_user_model.objects.create_user(**default_user_data)


@pytest.fixture
def logged_in_user(default_user_data, default_user, client):  # <.>
    client.login(default_user_data, "sekret")
    return default_user
