from enum import Enum

Suit = Enum('Suit', 'Diamonds Hearts Spades Clubs')
Value = Enum('Value', 'Ace 2 3 4 5 6 7 8 9 10 Jack Queen King')


class Card:
    __suit: Suit
    __value: Value
    __revealed: bool
    __owner = None

    def __init__(self, suit: Suit, value: Value, revealed: bool = False, owner=None):
        self.__suit = suit
        self.__value = value
        self.__revealed = revealed
        self.__owner = owner

    @property
    def suit(self) -> Suit:
        return self.__suit

    @property
    def value(self) -> Value:
        return self.__value

    @property
    def revealed(self) -> bool:
        return self.__revealed

    @revealed.setter
    def revealed(self, revealed: bool) -> None:
        self.__revealed = revealed

    @property
    def owner(self):
        return self.__owner

    @owner.setter
    def owner(self, owner) -> None:
        self.__owner = owner

    def __repr__(self) -> str:
        return f"{self.__value.name} of {self.__suit.name}"
