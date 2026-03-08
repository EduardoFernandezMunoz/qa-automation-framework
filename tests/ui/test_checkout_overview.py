import pytest
from pages.cart_page import CartPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login import LoginPage
import json

BASE_URL = "https://www.saucedemo.com"

def load_test_data():
    with open("data/test_data.json", encoding="utf-8") as f:
        return json.load(f)
test_data = load_test_data()

@pytest.mark.parametrize("user_data", test_data["valid_data"])
def test_checkout_overview(driver,user_data):
    driver.get(BASE_URL)

    login_page = LoginPage(driver)
    login_page.login(user_data["username"], user_data["password"])

    inventory_page = InventoryPage(driver)
    inventory_page.add_product_to_cart(user_data["product_name"])

    inventory_page.go_to_cart()

    cart_page = CartPage(driver)
    cart_page.checkout_button()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_checkout_info(user_data["first_name"], user_data["last_name"], user_data["zip_code"])

    checkout_page.submit_checkout_form()

    checkout_overview_page = CheckoutOverviewPage(driver)
    item = checkout_overview_page.get_product_name()

    assert "checkout-step-two" in driver.current_url, "Checkout overview page not found"
    assert item == user_data["product_name"], "Wrong product"

