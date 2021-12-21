from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement


class WikiHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def select_english_link(self):
        # this will return the web element with the given id
        element: WebElement = self.driver.find_element(By.ID, "js-link-box-en")
        return element

    def select_spanish_link(self):
        # this will return the web element with the given css selector
        element: WebElement = self.driver.find_element(By.CSS_SELECTOR, 'div[lang="es"]')
        return element

    def select_italian_link(self):
        # this will return the element found at the given xpath. Xpath is the most at-risk way of selecting
        # an element because it is the most likely to change, and therefore I do not recommend using it
        element: WebElement = self.driver.find_element(By.XPATH, "/html/body/div[2]/div[8]/a")
        return element

    # full_xpath = /html/body/div[2]/div[8]/a
    # relative xpath lets your driver make some assumptions
    # relative_xpath = //*[@id="js-link-box-it"

    def select_input_box(self):
        element: WebElement = self.driver.find_element(By.ID, "searchInput")
        return element

    def select_search_button(self):
        element: WebElement = self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
        return element

    def get_title_text(self):
        element: WebElement = self.driver.find_element(By.XPATH, '//*[@id="www-wikipedia-org"]/div[1]/h1/span')
        return element.text
