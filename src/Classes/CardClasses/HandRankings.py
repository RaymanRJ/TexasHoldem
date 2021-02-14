from enum import Enum
from Deck import Deck


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

def __is_royal_flush(deck: Deck) -> bool:
    return True