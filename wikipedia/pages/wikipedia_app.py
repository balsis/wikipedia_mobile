from allure_commons._allure import step
from selene import browser, have, be


@step('Type search')
def type_search(value):
    browser.element(("id", 'org.wikipedia:id/fragment_onboarding_skip_button')).click()
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
