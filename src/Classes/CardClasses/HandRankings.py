from enum import Enum
from src.Classes.CardClasses.Deck import Deck
from src.Classes.CardClasses.Card import Card, Suit, Value
from typing import Tuple, List, Union



class Rank(Enum):
    ROYAL_FLUSH = 1
    STRAIGHT_FLUSH = 2
    FOUR_OF_A_KIND = 3
    FULL_HOUSE = 4
    FLUSH = 5
    STRAIGHT = 6
    THREE_OF_A_KIND = 7
    TWO_PAIR = 8
    ONE_PAIR = 9
    HIGH_CARD = 10

class WinningRank:
    __rank: Rank
    __cards: List[Card]

    def __init__(self, rank: Rank, cards: List[Card]):
        self.rank = rank
        self.cards = cards

    @property
    def rank(self) -> Rank:
        return self.__rank

    @rank.setter
    def rank(self, rank: Rank) -> None:
        self.__rank = rank

    @property
    def cards(self) -> List[Card]:
        return self.__cards

    @cards.setter
    def cards(self, *cards) -> None:
        self.__cards.append(*cards)
        self.__sort_cards()

    def __sort_cards(self) -> None:
        self.cards.sort(key=lambda card: card.value)


def __is_flush(deck: Deck) -> Tuple[bool, Union[WinningRank, None]]:
    for suit in Suit:
        matches = [c for c in deck.cards if c.suit is suit]
        if len(matches) >= 5:
            return True, WinningRank(Rank.FLUSH, *matches)

    return False, None


def __is_straight(deck: Deck) -> Tuple[bool, Union[WinningRank, None]]:
    deck.cards.sort(key=lambda card: card.value)
    cards = deck.cards

    # Edge case: 10, J, Q, K, A --> A is considered a low card.
    values = [Value.ACE, Value.KING, Value.QUEEN, Value.JACK, Value.TEN]
    matches = 0
    for value in values:
        if any(c.Value for c in cards is value):
            matches += 1
    if matches >= 5:
        return True, WinningRank(Rank.STRAIGHT, cards)

    # five in a row
    for pos, card in enumerate(cards):
        if pos + 4 > 6:
            return False, None
        if cards[pos + 4].value == card.value + 4:
            return True, WinningRank(Rank.STRAIGHT, cards)

    return False, None


def __is_straight_flush(deck: Deck) -> Tuple[bool, Union[WinningRank, None]]:
    is_flush, wining_rank = __is_flush(deck)
    is_straight, winning_rank = __is_straight(deck)

    if is_straight and is_flush:
        return True, WinningRank(Rank.STRAIGHT_FLUSH, deck.cards)

    return False, None


def __is_royal_flush(deck: Deck) -> Tuple[bool, Union[WinningRank, None]]:
    is_straight_flush, winning_rank = __is_straight_flush(deck)
    if is_straight_flush:
        if winning_rank.cards[0].value is Value.ACE and winning_rank.cards[-4].value is Value.TEN:
            return True, winning_rank
    return False, None


def __get_pairs(deck: Deck) -> List[Card]:
    pairs = []
    for card in deck.cards:
        for second_card in deck.cards[1:]:
            if card.value == second_card.value:
                pairs.append()

def get_rank(deck: Deck) -> Rank:
    if __is_royal_flush(deck):
        return Rank.ROYAL_FLUSH
    if __is_straight_flush(deck):
        return Rank.STRAIGHT_FLUSH
    if __is_four_of_a_kind(deck):
        return Rank.FOUR_OF_A_KIND
    if __is_full_house(deck):
        return Rank.FULL_HOUSE
    if __is_flush(deck):
        return Rank.FLUSH
    if __is_straight(deck):
        return Rank.STRAIGHT
    if __is_three_of_a_kind(deck):
        return Rank.THREE_OF_A_KIND
    if __is_two_pair(deck):
        return Rank.TWO_PAIR
    if __is_one_pair(deck):
        return Rank.ONE_PAIR
    return Rank.HIGH_CARD


def __is_one_pair(deck: Deck) -> bool:
    for card in deck.cards:
        for second_card in deck.cards[1:]:
            if card.value == second_card.value:
                return True
    return False
def __is_royal_flush(deck: Deck) -> bool:
    # if any(deck.cards )
    return True