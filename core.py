from abc import ABC, abstractmethod
from glob import glob
from typing import Iterable


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
