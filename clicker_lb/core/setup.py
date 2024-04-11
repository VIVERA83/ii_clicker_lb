from clicker.clicker import Clicker
from core.logger import setup_logging
from core.settings import ClickerSettings


async def main():
    loger = setup_logging()
    password = ClickerSettings().base_pass
    for login in [
        "122serovayu287",
        # "122ivanovdyu748"
    ]:
        print(login, password)
        await Clicker(login, login, loger).run()


