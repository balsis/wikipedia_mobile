import dotenv
from pydantic.v1 import BaseSettings


class ProjectConfig(BaseSettings):
    bstack_userName: str
    bstack_accessKey: str
    timeout: int
    app_package: str = 'bs://8dd4ebcc3eff6c9d1a095dfdab65ddd332497ca7'
    bstack_remote_url: str = 'http://hub.browserstack.com/wd/hub'
    deviceName: str = "Google Pixel 3"
    platformVersion: str = "9.0"


config = ProjectConfig(dotenv.find_dotenv())
