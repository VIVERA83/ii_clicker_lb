import asyncio

from icecream import ic

from clicker.clicker import Clicker
from core.logger import setup_logging

courses = [2393,2310]
# a=2311, b = 2393, oop = 2310
users_data = [
"440lopatinke334",
"440lukinmn485",
"440magomedovim667",
"440matyuninaa365",
"440morokhovetsaa602",
"440myrzakulovma363",
"440nikiforoven595",
"440obraztsovkv467",
"440orlovip515",
"440paninvo937",
"440pantovichz212",
"440popovsn490",
"440rabievad955",
"440rasulovesh556",
"440rakhmanovia450",
]

async def main():
    for login in users_data:
        clicker = Clicker(login, "Magnit440*", setup_logging())
        ic(await clicker.run(courses))


if __name__ == "__main__":
    asyncio.run(main())
