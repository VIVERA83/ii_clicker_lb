import asyncio

from icecream import ic

from clicker.clicker import Clicker
from core.logger import setup_logging

courses = [2311]
# a=2311, b = 2393, oop = 2310,  siz=2317
users_data = [
"344pavlenkoiv121"
]


async def main():
    for login in users_data:
        clicker = Clicker(login, "Magnit344*", setup_logging())
        ic(await clicker.run(courses))
# "Magnit344*"

if __name__ == "__main__":
    asyncio.run(main())
