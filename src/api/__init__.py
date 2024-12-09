import os
from pathlib import Path

import requests
from dotenv import load_dotenv

load_dotenv()

BASE_URL = "https://adventofcode.com"
CACHE_DIR = ".input"


def get_input(year, day) -> str:
    file = Path(CACHE_DIR, f"{year}_{day}.txt")
    file.parent.mkdir(parents=True, exist_ok=True)

    if file.exists():
        return file.read_text()
    else:
        with requests.get(
            f"{BASE_URL}/{year}/day/{day}/input",
            cookies={"session": os.getenv("AOC_TOKEN")},
        ) as response:
            if not response.ok:
                raise Exception(response.text)

            data = response.text
            file.write_text(data)
            return data
