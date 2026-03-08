import pytest
from pages.inventory_page import InventoryPage
from pages.login import LoginPage
import json

BASE_URL = "https://www.saucedemo.com"

def load_test_data():
    with open("data/test_data.json", encoding="utf-8") as f:
        return json.load(f)
test_data = load_test_data()

@pytest.mark.parametrize("user_data", test_data["valid_data"])
def test_add_product_to_cart(driver,user_data):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(user_data["username"], user_data["password"])

    add_product_to_cart_page = InventoryPage(driver)
    remove_button = add_product_to_cart_page.add_product_to_cart(user_data["product_name"])

    assert remove_button == "Remove", "Add product failed"
    assert add_product_to_cart_page.cart_count() == "1", "Cart not updated"