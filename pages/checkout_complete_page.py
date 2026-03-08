from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class CheckoutCompletePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.order_completed_header = (By.CLASS_NAME, "complete-header")
        self.order_completed_message = (By.CLASS_NAME, "complete-text")

    def get_order_completed_header(self):
        return self.driver.find_element(*self.order_completed_header).text

    def get_order_completed_message(self):
        return self.driver.find_element(*self.order_completed_message).text