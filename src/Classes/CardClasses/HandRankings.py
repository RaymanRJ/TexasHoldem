from enum import Enum
from src.Classes.CardClasses.Deck import Deck
from src.Classes.CardClasses.Card import Card, Suit, Value
from typing import Tuple, List, Union, Callable, Dict


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

    def __init__(self, rank: Rank, *cards: Card):
        self.rank = rank
        self.__cards = [*cards]

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
    deck.cards.sort(key=lambda card: card.value.value)
    card_values = [c.value for c in deck.cards]

    # Edge case: 10, J, Q, K, A --> A is considered a low card.
    values = [Value.ACE, Value.KING, Value.QUEEN, Value.JACK, Value.TEN]
    matches = 0
    for value in values:
        if card_values.__contains__(value):
            matches += 1
    if matches >= 5:
        return True, WinningRank(Rank.STRAIGHT, *deck.cards)

    # five in a row
    for pos, card in enumerate(deck.cards):
        if pos + 4 > 6:
            return False, None
        if deck.cards[pos + 4].value.value == card.value.value + 4:
            return True, WinningRank(Rank.STRAIGHT, *deck.cards)

    return False, None


def __is_straight_flush(deck: Deck) -> Tuple[bool, Union[WinningRank, None]]:
    is_flush, wining_rank = __is_flush(deck)
    is_straight, winning_rank = __is_straight(deck)

    if is_straight and is_flush:
        return True, WinningRank(Rank.STRAIGHT_FLUSH, *deck.cards)

    return False, None


def __is_royal_flush(deck: Deck) -> Tuple[bool, Union[WinningRank, None]]:
    is_straight_flush, winning_rank = __is_straight_flush(deck)
    if is_straight_flush:
        royal_values = [Value.ACE, Value.KING, Value.QUEEN, Value.JACK, Value.TEN]
        deck_values = [card.value for card in deck.cards]
        for value in royal_values:
            if value not in deck_values:
                return False, None
        return True, WinningRank(Rank.ROYAL_FLUSH, *deck.cards)
    return False, None


def __is_four_of_a_kind(deck: Deck):
    matches = __get_value_matches(deck)
    for value, occurrences in matches.items():
        if occurrences == 4:
            return True, WinningRank(Rank.FOUR_OF_A_KIND, *deck.cards)
    return False, None


def __get_value_matches(deck: Deck) -> Dict[Value, int]:
    match_dict: Dict[Value, int] = dict()
    for card in deck.cards:
        if card.value in match_dict.keys():
            match_dict[card.value] = match_dict[card.value] + 1
        else:
            match_dict[card.value] = 1
    return match_dict


def __is_full_house(deck):
    matches = sorted(__get_value_matches(deck).items(), key=lambda item: item[1])
    found_a_triple = False
    for value in reversed(matches):
        if value[1] >= 3:
            if found_a_triple:
                return True, WinningRank(Rank.FULL_HOUSE, *deck.cards)
            else:
                found_a_triple = True
        elif value[1] >= 2:
            if found_a_triple:
                return True, WinningRank(Rank.FULL_HOUSE, *deck.cards)
    return False, None


def __is_three_of_a_kind(deck):
    matches = __get_value_matches(deck)
    for value, occurrences in matches.items():
        if occurrences >= 3:
            return True, WinningRank(Rank.THREE_OF_A_KIND, *deck.cards)
    return False, None


def __is_two_pair(deck):
    matches = __get_value_matches(deck)
    found_a_match = False
    for value, occurrences in matches.items():
        if occurrences >= 2:
            if found_a_match:
                return True, WinningRank(Rank.TWO_PAIR, *deck.cards)
            else:
                found_a_match = True
    return False, None


def __is_one_pair(deck):
    matches = __get_value_matches(deck)
    for value, occurrences in matches.items():
        if occurrences >= 2:
            return True, WinningRank(Rank.ONE_PAIR, *deck.cards)
    return False, None


def get_rank(deck: Deck) -> WinningRank:
    tests: List[Callable] = [
        __is_royal_flush,
        __is_straight_flush,
        __is_four_of_a_kind,
        __is_full_house,
        __is_flush,
        __is_straight,
        __is_three_of_a_kind,
        __is_two_pair,
        __is_one_pair
    ]

    for test in tests:
        passed, winning_rank = test(deck)
        if passed:
            return winning_rank

    return Rank.HIGH_CARD   # TODO: This.

