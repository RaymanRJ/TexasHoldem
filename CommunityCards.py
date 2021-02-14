from Deck import Deck, Card
from typing import List
from enum import Enum


class CommunityCards:
    __deck: Deck

    def __init__(self):
        self.__deck = Deck()

    def add_card(self, card: Card) -> None:
        card.revealed = True
        self.__deck.add_card(card)

    @property
    def cards(self) -> List[Card]:
        return self.__deck.cards
