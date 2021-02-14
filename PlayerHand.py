from Deck import Deck, Card
from HandRankings import *
from CommunityCards import CommunityCards


class PlayerHand:
    __hand: Deck
    __rank: Rank

    def __init__(self):
        self.__hand = Deck()

    def add_card(self, card: Card, shuffle: bool = True):
        self.__hand.add_card(card, shuffle)

    def calculate_rank(self, community_cards: CommunityCards) -> Rank:
        deck = Deck()
        for card in self.__hand.cards:
            deck.add_card(card)
        for card in community_cards.cards:
            deck.add_card(card)

        return get_rank(deck)
