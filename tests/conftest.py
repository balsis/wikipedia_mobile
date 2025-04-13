import allure
import pytest
from selene import browser
from appium import webdriver
from config import config
from wikipedia.helpers import attach


@pytest.fixture(scope = 'function', autouse = True)
def mobile_management():
    options = config.get_options()

    with allure.step('init app session'):
        browser.config.driver = webdriver.Remote(
            config.bstack_remote_url,
            options = options
        )
    browser.config.timeout = config.timeout
    yield
    attach.bstack_screenshot()
    attach.bstack_page_source_xml()

    session_id = browser.driver.session_id
    with allure.step('tear down app session'):
        browser.quit()

    attach.bstack_video(session_id)
