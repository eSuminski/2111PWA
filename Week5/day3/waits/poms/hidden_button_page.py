from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class HiddenButtonPage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def get_button_element(self):
        return self.driver.find_element(By.ID, "button")
