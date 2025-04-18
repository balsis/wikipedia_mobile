import os

import dotenv
from pydantic.v1 import BaseSettings, Field
from appium.options.android import UiAutomator2Options
from appium.options.ios import XCUITestOptions


env_type = os.getenv('ENV_TYPE', 'android').lower()
env_file = {
    'android': '.env.android',
    'ios': '.env.ios'
}.get(env_type)

dotenv.load_dotenv(dotenv_path = env_file)


class ProjectConfig(BaseSettings):
    platformName: str
    bstack_userName: str
    bstack_accessKey: str
    timeout: int
    app_package: str
    bstack_remote_url: str = 'http://hub.browserstack.com/wd/hub'
    deviceName: str
    platformVersion: str

    def get_options(self):
        capabilities = {
            'platformVersion': self.platformVersion,
            'deviceName': self.deviceName,
            'app': self.app_package,
            'bstack:options': {
                'projectName': 'Mobile project',
                'buildName': 'browserstack-build-1',
                'sessionName': f'{self.platformName} test',
                'userName': self.bstack_userName,
                'accessKey': self.bstack_accessKey,
            }
        }

        if self.platformName == 'android':
            return UiAutomator2Options().load_capabilities(capabilities)

        elif self.platformName == 'ios':
            return XCUITestOptions().load_capabilities(capabilities)

        else:
            raise ValueError(f'Unsupported platform: {self.platformName}')


config = ProjectConfig()
