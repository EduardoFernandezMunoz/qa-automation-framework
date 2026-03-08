from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutOverviewPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.item_name = (By.CLASS_NAME, "inventory_item_name")
        self.finish_button = (By. ID, "finish")

    def get_product_name(self):
        return self.driver.find_element(*self.item_name).text

    def finish_purchase(self):
        self.driver.find_element(*self.finish_button).click()