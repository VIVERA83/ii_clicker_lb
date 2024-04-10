import os
from typing import Literal

from pydantic import BaseModel, field_validator
from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))

LOG_LEVEL = Literal[
    "CRITICAL",
    "FATAL",
    "ERROR",
    "WARN",
    "WARNING",
    "INFO",
    "DEBUG",
    "NOTSET",
]


class Base(BaseSettings):
    class Config:
        """Settings for reading environment variables from a file.

        env_file - The path to the environment, to run locally
        """

        env_nested_delimiter = "__"
        env_file = os.path.join(BASE_DIR, ".env")
        enf_file_encoding = "utf-8"
        extra = "ignore"


class LogSettings(Base):
    """Setting logging.

    level (str, optional): The level of logging. Defaults to "INFO".
    guru (bool, optional): Whether to enable guru mode. Defaults to True.
    traceback (bool, optional): Whether to include tracebacks in logs. Defaults to True.
    """

    level: LOG_LEVEL = "INFO"
    guru: bool = True
    traceback: bool = True


class ClickerSettings(Base):
    """Settings for clicker.

    base_url (str, optional): The base URL of the clicker.
    login_url (str, optional): The login URL of the clicker.
    change_pass_url (str, optional): The change password URL of the clicker.
    db_b (str, optional): The path to file with data for b course.
    db_oop (str, optional): The path to file with data for oop course .
    """

    base_url: str
    login_url: str
    change_pass_url: str

    db_b: str
    test_id_b: int
    separator_b: str
    db_oop: str
    test_id_oop: int
    separator_oop: str
    base_pass: str

    @field_validator("db_b", "db_oop", mode="before")
    def str_to_date(cls, v: str) -> str:  # noqa:
        return os.path.join(BASE_DIR, "clicker_lb/static", v)
