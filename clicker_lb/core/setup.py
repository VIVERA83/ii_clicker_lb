from dataclasses import dataclass, field, asdict
from typing import Literal

from icecream import ic

from clicker.clicker import Clicker
from core.logger import setup_logging
from core.settings import ClickerSettings


@dataclass
class Result:
    status: Literal["OK", "ERROR"] = "OK"
    course: str = "Unknown course"
    result: list = field(default_factory=list)
    message: str = "Success"

    def to_dict(self):
        return asdict(self)


async def main():
    loger = setup_logging()
    login = "122serovayu287"
    password = ClickerSettings().base_pass
    result = Result()
    try:
        result.result.append(await Clicker(login, login, loger).run())
    except Exception as e:
        result.status = "ERROR"
        result.message = str(e)
    return ic(result)
