from typing import Dict

from src.Classes.MoneyClasses.Chip import Denomination, Chip


class ChipStack:
    __chip_stack: Dict[Denomination, int]

    def __init__(self, *chips: Chip):
        self.__chip_stack = dict(
            [
                (denomination, 0) for denomination in Denomination
            ]
        )

        for chip in chips:
            self.__chip_stack[chip.denomination] += 1

    @property
    def value(self) -> int:
        return sum(chip[0].value * chip[1] for chip in self.__chip_stack.items())
