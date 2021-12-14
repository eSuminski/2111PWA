from behave import Given, When, Then


@Given(u'the user is on the homepage')
def step_impl(context):
    context.driver.get("https://www.wikipedia.org/")


@When(u'the user inputs {value} into the search bar')
def step_impl(context, value: str):
    context.wiki_home.select_input_box().send_keys(value)


@When(u'the user clicks the search button')
def step_impl(context):
    context.wiki_home.select_search_button().click()


@Then(u'the user should be redirected to a webpage with the title {title}')
def step_impl(context, title: str):
    assert context.driver.title == title


# @When(u'the user inputs puppy into the search bar')
# def step_impl(context):
#     context.wiki_home.select_input_box().send_keys("puppy")
#
#
# @Then(u'the user should be redirected to a webpage with the title Puppy - Wikipedia')
# def step_impl(context):
#     assert context.driver.title == "Puppy - Wikipedia"
#
#
# @When(u'the user inputs pacman into the search bar')
# def step_impl(context):
#     context.wiki_home.select_input_box().send_keys("pacman")
#
#
# @Then(u'the user should be redirected to a webpage with the title Pac-Man - Wikipedia')
# def step_impl(context):
#     assert context.driver.title == "Pac-Man - Wikipedia"
