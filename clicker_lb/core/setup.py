from clicker.clicker import Clicker
from core.logger import setup_logging
from core.settings import ClickerSettings


async def main():
    loger = setup_logging()
    password = ClickerSettings().base_pass
    for login in [
        "122shmakovvi800"
    ]:
        await Clicker(login, "122shmakovvi800", loger).run()
