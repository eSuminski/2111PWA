from behave.runner import Context
from selenium import webdriver
from poms.hidden_button_page import HiddenButtonPage


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.hidden_button_page = HiddenButtonPage(context.driver)
    # an implicit wait makes it so your test will wait UP TO the number of seconds you provide for
    # any action to be able to be completed
    # HIGHLY recommend you set an implicit wait, even if it is for half a second, to make sure a poor internet
    # connection does not make your test fail
    context.driver.implicitly_wait(4)


def after_all(context: Context):
    context.driver.quit()
