from logging import Logger, getLogger

from selenium import webdriver
from selenium.webdriver.common.by import By

from clicker.utils import wait_random_time, get_chrome_options
from core.settings import ClickerSettings

BASE_URL = ClickerSettings().base_url


class BaseClicker:

    def __init__(self, logger: Logger = getLogger(__name__)):
        self.logger = logger
        self.driver = webdriver.Chrome(options=get_chrome_options())

    @wait_random_time(min_sec=2, max_sec=3)
    async def set_value_input(self, name: str, value: str, by: By = By.XPATH):
        input_field = self.driver.find_element(by=by, value=name)
        input_field.send_keys(value)

    @wait_random_time(min_sec=5, max_sec=10)
    async def click(self, name: str, by: By = By.XPATH):
        self.driver.find_element(by=by, value=name).click()

    @staticmethod
    def create_url(prefix: str = "", **params) -> str:
        url = BASE_URL + prefix
        if params:
            url += "?" + "&".join([
                f"{key}={val}"
                for key, val in params.items()
            ])
        return url

    def close(self):
        self.driver.quit()
