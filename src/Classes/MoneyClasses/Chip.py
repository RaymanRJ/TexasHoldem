from enum import Enum
from typing import List


class Denomination(Enum):
    ONE = 1
    FIVE = 5
    TEN = 10
    TWENTY = 20
    FIFTY = 50
    HUNDRED = 100


class Chip:
    __denomination: Denomination

    def __init__(self, denomination: Denomination):
        self.__denomination = denomination

    @property
    def denomination(self) -> Denomination:
        return self.__denomination

    @property
    def value(self) -> int:
        return self.__denomination.value

    def __eq__(self, other) -> bool:
        return self.denomination == other.denomination

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __gt__(self, other) -> bool:
        return self.value > other.value

    @staticmethod
    def get_chips(value: int):
        chips: List[Chip] = list()
        for denomination in reversed(Denomination):
            while value >= denomination.value:
                chips.append(Chip(denomination))
                value -= denomination.value
        return chips
