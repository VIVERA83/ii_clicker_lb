from logging import Logger

from clicker.base import BaseClicker
from clicker.utils import wait_random_time
from core.settings import ClickerSettings

LOGIN_URL = ClickerSettings().login_url
CHANGE_PASS_URL = ClickerSettings().change_pass_url


class AUTHClicker(BaseClicker):

    def __init__(self, login: str, password: str, logger: Logger = None):
        super().__init__(logger)
        self.login = login
        self.password = password

    @wait_random_time()
    async def log_in(self, new_password: str = "1234qwer"):
        self.driver.get(LOGIN_URL)
        await self._log_in()
        if self.driver.current_url == CHANGE_PASS_URL:
            await self._change_password(new_password)

    async def _log_in(self):
        await self.set_value_input('//*[@id="username"]', self.login)
        await self.set_value_input('//*[@id="password"]', self.password)
        await self.click('//*[@id="loginbtn"]')
        self.logger.info("Log in: ok!")

    async def _change_password(self, new_password: str):
        await self.set_value_input('//*[@id="id_password"]', self.password)
        await self.set_value_input('//*[@id="id_newpassword1"]', new_password)
        await self.set_value_input('//*[@id="id_newpassword2"]', new_password)
        await self.click('//*[@id="id_politic"]')
        await self.click('//*[@id="id_submitbutton"]')
        self.logger.info("change password: ok!")
