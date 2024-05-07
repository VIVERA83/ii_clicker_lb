import os
from typing import Literal

from pydantic import SecretStr, field_validator
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
        env_file = os.path.join(BASE_DIR, ".env_labor_protect")
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

    db_a: str
    test_id_a: int
    separator_a: str

    db_b: str
    test_id_b: int
    separator_b: str

    db_oop: str
    test_id_oop: int
    separator_oop: str

    db_siz: str
    test_id_siz: int
    separator_siz: str

    base_pass: str

    @field_validator("db_a", "db_b", "db_oop", "db_siz", mode="before")
    def str_to_date(cls, v: str) -> str:  # noqa:
        return os.path.join(BASE_DIR, "clicker_lb/static", v)


class RabbitMQSettings(Base):
    rabbit_user: str
    rabbit_password: SecretStr
    rabbit_host: str
    rabbit_port: int

    def dsn(self, show_secret: bool = False) -> str:
        """Returns the connection URL as a string.

        Args:
            show_secret (bool, optional): Whether to show the secret. Defaults to False.

        Returns:
            str: The connection URL.
        """
        return "amqp://{user}:{password}@{host}:{port}/".format(
            user=self.rabbit_user,
            password=(
                self.rabbit_password.get_secret_value()
                if show_secret
                else self.rabbit_password
            ),
            host=self.rabbit_host,
            port=self.rabbit_port,
        )
