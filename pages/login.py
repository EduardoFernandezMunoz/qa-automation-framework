import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage
from utils.driver_factory import get_driver

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.username = (By.ID, "user-name")
        self.password = (By.ID, "password")
        self.submit_button = (By.ID, "login-button")


    def login(self, username, password):
        self.driver.find_element(*self.username).send_keys(username)
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.submit_button).click()