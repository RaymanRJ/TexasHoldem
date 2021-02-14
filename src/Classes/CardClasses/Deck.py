from typing import List
from itertools import product
from random import shuffle
from Card import Card, Suit, Value


class Deck:
    __cards: List[Card] = []

    def __init__(self, cards: List[Card] = None):
        self.__cards = []
        if cards is not None:
            for card in cards:
                self.__cards.append(card)

    def add_card(self, card: Card, shuffle: bool = False) -> None:
        self.__cards.append(card)
        if shuffle:
            self.shuffle_deck()

    def draw_card(self, shuffle: bool = False) -> Card:
        card = self.__cards.pop()
        if shuffle:
            self.shuffle_deck()
        return card

    def shuffle_deck(self) -> None:
        shuffle(self.__cards)

    def print(self) -> None:
        for card in self.__cards:
            print(card)

    @property
    def cards(self) -> List[Card]:
        return self.__cards

    @staticmethod
    def create_new_deck(shuffle_deck: bool = True):
        deck = Deck()

        for suit, value in product(Suit, Value):
            deck.add_card(Card(suit, value))

        if shuffle_deck:
            deck.shuffle_deck()
        return deck
