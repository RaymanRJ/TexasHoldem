from Actor import Actor
from CommunityCards import CommunityCards
from src.Classes.CardClasses.HandRankings import *


class Player(Actor):

    __community_cards: CommunityCards

    def __init__(self, name: str, community_cards: CommunityCards, deck: Deck = None):
        super().__init__(name, deck)
        self.__community_cards = community_cards

    def get_rank(self) -> Rank:
        #TODO: Fix this logic.
        return get_rank()

    def __repr__(self) -> str:
        return self.name

    def bet(self) -> int:
        return 10
        #TODO: Implement betting