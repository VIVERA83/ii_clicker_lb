import json
from dataclasses import asdict, dataclass, field
from typing import Literal

from clicker.clicker import Clicker
from core.logger import setup_logging


@dataclass
class Result:
    user: str = "Пользователь не найден"
    status: Literal["OK", "ERROR"] = "OK"
    course: str = ""
    result: list = field(default_factory=list)
    message: str = "Успешно"

    def to_dict(self):
        return asdict(self)


async def execute_rpc_action(login: str, password: str, course_type: Literal[2311, 2393, 2310]) -> str:
    """Asynchronously runs a program for a specific course type.

    Parameters:
    - login (str): The login username.
    - password (str): The password for the login.
    Raises:
    - Exception: If the course is not found.
    Returns:
    - None
    """
    clicker = Clicker(login, password, setup_logging())
    try:
        result = Result(course="Labor protect course")
        result.result.append(await clicker.run([course_type]))
    except Exception as ex:
        raise Exception(ex.args[0])
    finally:
        clicker.close()
    return json.dumps(
        Result(
            user=login,
            status="ERROR",
            course="course_type",
            result=[],
            message="Неизвестный тип курса",
        ).to_dict()
    )
