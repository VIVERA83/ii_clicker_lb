import asyncio

from icecream import ic

from clicker.clicker import Clicker
from core.logger import setup_logging

courses = [2310,2393]
# a=2311, b = 2393, oop = 2310
users_data = [
"344tsvetkovsg279",
]


async def main():
    for login in users_data:
        clicker = Clicker(login, "344tsvetkovsg279", setup_logging())
        ic(await clicker.run(courses))


if __name__ == "__main__":
    asyncio.run(main())
