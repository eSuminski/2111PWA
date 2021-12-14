from behave.runner import Context
from selenium import webdriver
from page_object_models.wiki_page import WikiHomePage


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.wiki_home = WikiHomePage(context.driver)


def after_all(context):
    context.driver.quit()
