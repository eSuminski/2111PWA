from behave import Given, When, Then

@Given(u'The English user is on the wikipedia home page')
def get_wiki_home(context):
    context.driver.get("https://www.wikipedia.org/")


@When(u'The English user clicks on the english link')
def click_english_link(context):
    context.wiki_home.select_english_link().click()


@Then(u'The English user should be redirected to the english home page')
def check_english_title(context):
    title = context.driver.title
    assert title == "Wikipedia, the free encyclopedia"


@Given(u'The Spanish user is on the wikipedia home page')
def get_home_page_spanish(context):
    context.driver.get("https://www.wikipedia.org/")


@When(u'The Spanish user clicks on the spanish link')
def click_spanish_link(context):
    context.wiki_home.select_spanish_link().click()


@Then(u'The Spanish user should be redirected to the spanish home page')
def check_spanish_title(context):
    title = context.driver.title
    assert title == "Wikipedia, la enciclopedia libre"


@Given(u'The Italian user is on the wikipedia home page')
def get_home_page_italian(context):
    context.driver.get("https://www.wikipedia.org/")


@When(u'The Italian user clicks on the italian link')
def click_italian_link(context):
    context.wiki_home.select_italian_link().click()


@Then(u'The Italian user should be redirected to the italian home page')
def step_impl(context):
    title = context.driver.title
    assert title == "Wikipedia, l'enciclopedia libera"
