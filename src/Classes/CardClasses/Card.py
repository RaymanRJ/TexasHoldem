from enum import Enum


class Suit(Enum):
    DIAMONDS = 0
    HEARTS = 1
    SPADES = 2
    CLUBS = 3


class Value(Enum):
    ACE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9
    TEN = 10
    JACK = 11
    QUEEN = 12
    KING = 13


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
