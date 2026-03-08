import json
import pytest
from api.jsonplaceholder_api import JSONPlaceholderAPI


def load_test_data():
    with open("data/test_data.json", encoding="utf-8") as f:
        return json.load(f)


test_data = load_test_data()


def test_get_posts_by_user():
    """
    Verify that posts can be retrieved for a specific user.

    Steps:
    1. Send GET request to /posts with query parameter userId=5.
    2. Verify the response status code is 200.
    3. Verify the response body is a list of posts.
    4. Verify all returned posts belong to the requested user.
    """

    api = JSONPlaceholderAPI()

    response = api.get_posts_by_user_id(5)
    body = response.json()

    assert response.status_code == 200
    assert isinstance(body, list)
    assert len(body) > 0

    for post in body:
        assert post["userId"] == 5


@pytest.mark.parametrize("post_data", test_data["api_posts"])
def test_create_post(post_data):
    """
    Verify that a new post can be created using different payloads.

    Steps:
    1. Send POST request to /posts with a valid payload.
    2. Verify the response status code is 201.
    3. Verify the returned post contains the same data as the payload.
    """

    api = JSONPlaceholderAPI()

    response = api.create_post(post_data)
    body = response.json()

    assert response.status_code == 201
    assert "id" in body
    assert body["title"] == post_data["title"]
    assert body["body"] == post_data["body"]
    assert body["userId"] == post_data["userId"]