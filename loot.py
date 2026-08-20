from pyray import *
from uuid import UUID, uuid4
from random import randint

class Loot:
    def __init__(self, value: int, name: str) -> None:
        self.value: int = value
        self.name: str = name

class Amber(Loot):
    def __init__(self, value: int, name: str) -> None:
        super().__init__(value, name)
        self.washed: bool = False
        self.smoothed: bool = False
        self.polished: bool = False

    def wash(self) -> None:
        if not self.washed:
            self.value += self.value // 4
            self.washed = True

    def smooth(self) -> None:
        if not self.smoothed:
            self.value += self.value // 2
            self.smoothed = True

    def polish(self) -> None:
        if not self.polished:
            self.value += self.value // 2
            self.polished = True

class Pile:
    def __init__(self) -> None:
        self.id: UUID = uuid4()
        self.searches: int = randint(3, 5)

    def search(self) -> int:
        if self.searches > 0:
            self.searches -= 1

        return self.searches
