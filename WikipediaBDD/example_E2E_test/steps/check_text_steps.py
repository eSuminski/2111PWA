from behave import Then

@Then(u'the title should have text')
def step_impl(context):
    assert context.wiki_home.get_title_text() == "Wikipedia"
