from Actor import Actor
from Card import Card


class CommunityCards(Actor):

    def __init__(self, name: str = "CommunityCards"):
        super().__init__(name)

    def add_card(self, *cards: Card) -> None:
        for card in cards:
            card.revealed = True
            super().add_card(card)
