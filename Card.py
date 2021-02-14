from enum import Enum
from Actor import Actor


Suit = Enum('Suit', 'Diamonds Hearts Spades Clubs')
Value = Enum('Value', 'Ace 2 3 4 5 6 7 8 9 10 Jack Queen King')


class Card:
    __suit: Suit
    __value: Value
    __revealed: bool
    __owning_actor: Actor

    def __init__(self, suit: Suit, value: Value, owning_actor: Actor, revealed: bool = False):
        self.__suit = suit
        self.__value = value
        self.__revealed = revealed
        self.__owning_actor = owning_actor

    @property
    def suit(self) -> Suit:
        return self.__suit

    @property
    def value(self) -> Value:
        return self.__value

    @property
    def owning_actor(self) -> Actor:
        return self.__owning_actor

    @property
    def revealed(self) -> bool:
        return self.__revealed

    @revealed.setter
    def revealed(self, val: bool) -> None:
        self.__revealed = val

    def __repr__(self) -> str:
        return f"{self.__value.name} of {self.__suit.name}"
