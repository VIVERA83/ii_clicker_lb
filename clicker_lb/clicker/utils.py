import asyncio
import json
import logging
from json import JSONDecodeError
from random import randint

from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_chrome_options() -> Options:
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size=1920,1080")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--headless=new")
    options.add_argument("--start-maximized")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--allow-running-insecure-content")
    user_agent = UserAgent(browsers=["chrome"]).getRandom.get("useragent")
    options.add_argument(f"user-agent={user_agent}")
    return options


def wait_random_time(min_sec: int = 5, max_sec: int = 10):
    def inner(func):
        async def wrapper(*args, **kwargs):
            result = await func(*args, **kwargs)
            await asyncio.sleep(randint(min_sec, max_sec))
            return result

        return wrapper

    return inner


def load_from_file(filename: str) -> dict:
    try:
        with open(filename, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.warning(f"File not found: {filename}")
    except JSONDecodeError:
        logging.warning(f"File data error: {filename}")
    return {}


def save_to_file(filename: str, data: dict[str, str]):
    try:
        with open(filename, "w") as f:
            return json.dump(data, f)
    except FileNotFoundError:
        logging.warning(f"File not found: {filename}")


