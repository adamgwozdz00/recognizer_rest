import pathlib
from pathlib import Path


def get_path() -> Path:
    return pathlib.Path(__file__).parent.parent.joinpath("app.log")
