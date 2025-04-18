from allure_commons._allure import step
from selene import browser, have, be


@step('Skip onboarding')
def skip_onboarding():
    browser.element(("id", 'org.wikipedia:id/fragment_onboarding_skip_button')).click()


@step('Type search')
def type_search(value):
    browser.element(("accessibility id", "Search Wikipedia")).click()
    browser.element(("id", "org.wikipedia:id/search_src_text")).type(value)


@step("Verify content found")
def verify_content_found(value):
    results = browser.all(("id", 'org.wikipedia:id/page_list_item_title'))
    results.should(have.size_greater_than(0))
    results.first.should(have.text(value))


@step("Open article")
def open_article(value):
    browser.all(("id", 'org.wikipedia:id/page_list_item_title')).first.click()
    browser.element(("xpath", f'//android.widget.TextView[@text="{value}"]')).should(be.visible)


@step("Next onboarding step")
def continue_onboarding():
    browser.element(('id', 'org.wikipedia:id/fragment_onboarding_forward_button')).click()


@step("Validate first onboarding view")
def validate_first_onboarding_view():
    browser.element(('id', 'org.wikipedia:id/primaryTextView')).should(have.text("The Free Encyclopedia"))


@step("Validate second onboarding view")
def validate_second_onboarding_view():
    browser.element(('id', 'org.wikipedia:id/primaryTextView')).should(have.text("New ways to explore"))


@step("Validate third onboarding view")
def validate_third_onboarding_view():
    browser.element(('id', 'org.wikipedia:id/primaryTextView')).should(have.text("Reading lists with sync"))


@step("Validate fourth onboarding view")
def validate_fourth_onboarding_view_and_accept_button():
    browser.element(('id', 'org.wikipedia:id/primaryTextView')).should(have.text("Send anonymous data"))
    browser.element(('id', 'org.wikipedia:id/acceptButton')).click()
