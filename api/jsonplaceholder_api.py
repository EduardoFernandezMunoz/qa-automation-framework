import requests


class JSONPlaceholderAPI:

    BASE_URL = "https://jsonplaceholder.typicode.com"

    def get_all_users(self):
        return requests.get(f"{self.BASE_URL}/users")

    def get_user_by_id(self, user_id):
        return requests.get(f"{self.BASE_URL}/users/{user_id}")

    def get_posts_by_user_id(self, user_id):
        return requests.get(f"{self.BASE_URL}/posts", params={"userId": user_id})

    def create_post(self, payload):
        return requests.post(f"{self.BASE_URL}/posts", json=payload)