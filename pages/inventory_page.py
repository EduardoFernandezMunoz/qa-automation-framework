from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class InventoryPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.item_number = (By.CLASS_NAME, "shopping_cart_badge")
        self.cart_button = (By.CLASS_NAME, "shopping_cart_link")

    def add_product_to_cart (self, product_name):
        products = self.driver.find_elements(By.CLASS_NAME, "inventory_item")
        for product in products:
            name = product.find_element(By.CLASS_NAME, "inventory_item_name").text
            if name == product_name:
                button = product.find_element(By.XPATH, ".//button[text()='Add to cart']")
                button.click()
                remove_button = product.find_element(By.XPATH, ".//button[text()='Remove']")
                return remove_button.text

    def cart_count (self):
        return self.driver.find_element(*self.item_number).text

    def go_to_cart(self):
        self.driver.find_element(*self.cart_button).click()