import pytest
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.login import LoginPage
import json

BASE_URL = "https://www.saucedemo.com"

def load_test_data():
    with open("data/test_data.json", encoding="utf-8") as f:
        return json.load(f)
test_data = load_test_data()

@pytest.mark.parametrize("user_data", test_data["valid_data"])
def test_product_is_displayed_in_cart(driver,user_data):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(user_data["username"], user_data["password"])

    add_product_to_cart_page = InventoryPage(driver)
    add_product_to_cart_page.add_product_to_cart(user_data["product_name"])

    add_product_to_cart_page.go_to_cart()
    assert "cart" in driver.current_url, "Cart page not found"

    cart_page = CartPage(driver)
    item = cart_page.get_product_name()

    assert item == user_data["product_name"], "Wrong product"