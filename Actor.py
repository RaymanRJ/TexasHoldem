
# Actors are anyone that can hold a deck:
# - Players
# - Community Cards
# - Game object

from Deck import Deck
from Card import Card


class Actor:
    __name: str
    __deck: Deck

    def __init__(self, name: str, deck: Deck = None):
        self.__name = name
        self.__deck = deck if deck is not None else Deck()

    @property
    def name(self) -> str:
        return self.__name

    @property
    def deck(self) -> Deck:
        return self.__deck

    def add_card(self, card: Card) -> None:
        card.owner = self
        self.__deck.add_card(card)
        print(f"Actor {self.name} added a new card.")

