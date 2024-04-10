import os

from pydantic import BaseModel
from pydantic_settings import BaseSettings

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__name__)))

class Base(BaseSettings):
    class Config:
        """Settings for reading environment variables from a file.

        env_file - The path to the environment, to run locally
        """

        env_nested_delimiter = "__"
        env_file = os.path.join(BASE_DIR, ".env")
        enf_file_encoding = "utf-8"
        extra = "ignore"