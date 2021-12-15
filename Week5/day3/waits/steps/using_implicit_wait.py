from behave import Given, When, Then
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException


@Given(u'I am on the webpage with the hidden button')
def step_impl(context):
    context.driver.get("file:///C:/Users/EricSuminski/Desktop/2111PWA/Week5/day3/hidden_element.html")


@When(u'I click the button that says click me')
def step_impl(context):
    # WebDriverWait = my object that controls the wait time
    # context.driver = the driver we provide via the environment module
    # 4 = the time to wait
    # .until() = method we need to call to tell our object when it can stop waiting
    # expected_conditions = telling our wait object what it is going to be waiting for
    # visibility_of_element_located() = the criteria of what we are waiting for
    # By.ID = the element selector we are using
    # "button" = the value of the element selector we are looking for
    # explicit_wait = WebDriverWait(context.driver,4).until(
    #     expected_conditions.visibility_of_element_located(
    #         (By.ID,"button")
    #     )
    # )
    # fluent waits work like explicit waits, but you have more fine-tuned control over them
    # fluent_wait = WebDriverWait(
    #     context.driver,
    #     4,
    #     # the frequency which the driver will attempt to perform its action
    #     poll_frequency=1,
    #     # the explicit exceptions we want our test to ignore during the waiting period
    #     ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException]).until(
    #     expected_conditions.visibility_of_element_located(
    #         (By.ID,"button")
    #     )
    # )
    context.hidden_button_page.get_button_element().click()


@Then(u'I should see an alert that says good job')
def step_impl(context):
    alert = Alert(context.driver)
    assert alert.text == "good job!"
