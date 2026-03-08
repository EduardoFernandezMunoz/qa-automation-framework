import pytest
from pages.login import LoginPage
import json

BASE_URL = "https://www.saucedemo.com"

def load_test_data():
    with open("data/test_data.json", encoding="utf-8") as f:
        return json.load(f)
test_data = load_test_data()

@pytest.mark.parametrize("user_data", test_data["valid_data"])
def test_valid_login(driver, user_data):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(user_data["username"], user_data["password"])

    assert "inventory" in driver.current_url, "Login failed"

@pytest.mark.parametrize("user_data", test_data["invalid_data"])
def test_invalid_login(driver, user_data):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(user_data["username"], user_data["password"])

    assert "inventory" not in driver.current_url, "User should not be able to login"