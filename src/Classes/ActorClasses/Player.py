from src.Classes.ActorClasses.Actor import Actor
from src.Classes.ActorClasses.CommunityCards import CommunityCards
from src.Classes.CardClasses.HandRankings import *
from src.Classes.MoneyClasses.ChipStack import ChipStack


class Player(Actor):

    __community_cards: CommunityCards
    __is_all_in: bool
    __chips: ChipStack

    def __init__(self, name: str, community_cards: CommunityCards, deck: Deck = None):
        super().__init__(name, deck)
        self.__community_cards = community_cards
        self.__is_all_in = False
        self.__chips = ChipStack()

    def get_rank(self) -> Rank:
        #TODO: Fix this logic.
        return get_rank()

    def __repr__(self) -> str:
        return self.name

    def bet(self) -> int:
        return 10
        #TODO: Implement betting