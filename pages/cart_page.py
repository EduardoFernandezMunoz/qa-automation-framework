from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.item = (By.CLASS_NAME, "inventory_item_name")
        self.checkout = (By.ID, "checkout")


    def get_product_name(self):
        item = self.driver.find_element(*self.item).text
        return item

    def checkout_button(self):
        self.driver.find_element(*self.checkout).click()