import json
from abc import ABC, abstractmethod
from glob import glob
from typing import Any, Iterable


def load_modules(group: str):
    return list(
        map(
            lambda installable: installable(),
            map(
                lambda module: getattr(
                    getattr(__import__(f"{group}.{module}"), module), module
                ),
                map(
                    lambda path: path.replace("\\", ".")
                    .replace("/", ".")
                    .split(".")[1],
                    glob(f"{group}/*.py"),
                ),
            ),
        )
    )


def read_data(file: str) -> dict[str, Any]:
    try:
        return json.load(open(f"data/{file}.json", "r"))
    except:
        open(f"data/{file}.json", "x")
        return {}


def write_data(file: str, data: dict[str, Any]) -> None:
    return json.dump(data, open(f"data/{file}.json", "w"))


def set_data(file: str, key: str, value: Any) -> None:
    data = read_data(file)
    data[key] = value
    return write_data(file, data)


class Installable(ABC):
    @staticmethod
    @abstractmethod
    def install() -> "Installable":
        pass


class Trigger(Installable):
    @abstractmethod
    def on_second(self, second: int):
        pass

    @abstractmethod
    def on_occupied(self):
        pass

    @abstractmethod
    def on_available(self):
        pass


class Monitor(Installable):
    @abstractmethod
    def on_update(self, triggers: Iterable[Trigger]) -> None:
        pass
