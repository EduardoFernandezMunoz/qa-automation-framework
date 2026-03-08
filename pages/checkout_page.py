from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.first_name = (By.ID, "first-name")
        self.last_name = (By.ID, "last-name")
        self.zip_code = (By.ID, "postal-code")
        self.checkout_button = (By.ID, "continue")

    def fill_checkout_info(self, first_name, last_name, zip_code):
        self.driver.find_element(*self.first_name).send_keys(first_name)
        self.driver.find_element(*self.last_name).send_keys(last_name)
        self.driver.find_element(*self.zip_code).send_keys(zip_code)

    def submit_checkout_form(self):
        self.driver.find_element(*self.checkout_button).click()

