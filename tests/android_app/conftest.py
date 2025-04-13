import allure
import pytest
from appium.options.android import UiAutomator2Options
from selene import browser

from appium import webdriver

from config import config
from wikipedia.helpers import attach


@pytest.fixture(scope = 'function', autouse = True)
def mobile_management():
    options = UiAutomator2Options().load_capabilities({

        'platformVersion': config.platformVersion,
        'deviceName': config.deviceName,

        'app': config.app_package,

        'bstack:options': {
            'projectName': 'First mobile project',
            'buildName': 'browserstack-build-1',
            'sessionName': 'BStack first_test',

            'userName': config.bstack_userName,
            'accessKey': config.bstack_accessKey,
        }
    })

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
