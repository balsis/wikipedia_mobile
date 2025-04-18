import os
from pathlib import Path

from wikipedia.helpers import resource
from dotenv import load_dotenv
from pydantic.v1 import BaseSettings
from appium.options.android import UiAutomator2Options


class ProjectConfig(BaseSettings):
    context = "bstack"
    platformName: str
    bstack_userName: str = None
    bstack_accessKey: str = None
    app_package: str
    remote_url: str = 'http://hub.browserstack.com/wd/hub'
    deviceName: str
    platformVersion: str = None
    timeout: int = 10

    def get_options(self):
        capabilities = {
            'platformVersion': self.platformVersion,
            'deviceName': self.deviceName,
            'app': config.app_package if config.app_package.startswith('bs://') else resource.path(self.app_package),
            'appWaitActivity': "org.wikipedia.*"
        }

        if self.context == 'bstack':
            capabilities['bstack:options'] = {
                'projectName': 'Mobile project',
                'buildName': 'browserstack-build-1',
                'sessionName': f'{self.platformName} test',
                'userName': self.bstack_userName,
                'accessKey': self.bstack_accessKey,
            }

        if self.platformName == 'android':
            return UiAutomator2Options().load_capabilities(capabilities)
        else:
            raise ValueError(f'Unsupported platform: {self.platformName}')


def get_config():
    context = os.getenv('context', 'bstack')
    load_dotenv(dotenv_path = f'.env.{context}')
    if context == 'bstack':
        load_dotenv(dotenv_path = Path('.env.creds'), override = True)
    local_config = ProjectConfig(_env_file = Path(f'.env.{context}'))
    local_config.context = context
    return local_config


config = get_config()
