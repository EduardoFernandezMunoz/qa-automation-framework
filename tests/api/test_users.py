from api.jsonplaceholder_api import JSONPlaceholderAPI


def test_get_all_users():
    """
    Verify that the API returns the list of all users.

    Steps:
    1. Send GET request to /users endpoint.
    2. Verify the response status code is 200.
    3. Verify the response body is a list.
    4. Verify the list contains at least one user.
    """

    api = JSONPlaceholderAPI()

    response = api.get_all_users()
    body = response.json()

    assert response.status_code == 200
    assert isinstance(body, list)
    assert len(body) > 0


def test_get_user_by_id():
    """
    Verify that a specific user can be retrieved by ID.

    Steps:
    1. Send GET request to /users/{id}.
    2. Verify the response status code is 200.
    3. Verify the returned user has the expected ID.
    4. Verify the response contains important fields like name and email.
    """

    api = JSONPlaceholderAPI()

    response = api.get_user_by_id(1)
    body = response.json()

    assert response.status_code == 200
    assert body["id"] == 1
    assert "name" in body
    assert "email" in body