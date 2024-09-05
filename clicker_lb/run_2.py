import asyncio

from icecream import ic

from clicker.clicker import Clicker
from core.logger import setup_logging

courses = [2310,2393]
# a=2311, b = 2393, oop = 2310
users_data = [
"344ignatenkoav017",
"344kolesovan698",
"344kuznetsovso251",
"344kuptsovvp626",
"344lopatinsa368",
"344minaevrv108",
"344naumovsg952",
"344nesvitda267",
"344ozharovskijda138",
"344oreshnikovam349",
]


async def main():
    for login in users_data:
        clicker = Clicker(login, "Magnit344*", setup_logging())
        ic(await clicker.run(courses))


if __name__ == "__main__":
    asyncio.run(main())
