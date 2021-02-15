import unittest
from src.Classes.CardClasses.Deck import Deck
from src.Classes.CardClasses.Card import Card, Suit, Value
from src.Classes.CardClasses.HandRankings import *


class TestHandRank(unittest.TestCase):

    def setUp(self) -> None:
        self.royal_flush_cards = [
            Card(Suit.DIAMONDS, Value.ACE),
            Card(Suit.DIAMONDS, Value.KING),
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.DIAMONDS, Value.TEN),
            Card(Suit.DIAMONDS, Value.TWO),
            Card(Suit.DIAMONDS, Value.THREE),
        ]
        self.straight_flush_cards = [
            Card(Suit.DIAMONDS, Value.KING),
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.DIAMONDS, Value.TEN),
            Card(Suit.DIAMONDS, Value.NINE),
            Card(Suit.DIAMONDS, Value.TWO),
            Card(Suit.DIAMONDS, Value.THREE),
        ]
        self.flush_cards = [
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.DIAMONDS, Value.TEN),
            Card(Suit.DIAMONDS, Value.NINE),
            Card(Suit.DIAMONDS, Value.FIVE),
            Card(Suit.CLUBS, Value.TWO),
            Card(Suit.CLUBS, Value.THREE),
        ]
        self.straight_cards = [
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.CLUBS, Value.TEN),
            Card(Suit.SPADES, Value.NINE),
            Card(Suit.DIAMONDS, Value.EIGHT),
            Card(Suit.CLUBS, Value.TWO),
            Card(Suit.CLUBS, Value.THREE),
        ]

        self.cards = [
            self.royal_flush_cards,
            self.straight_flush_cards,
            self.flush_cards,
            self.straight_cards
        ]

    def test_straight_flush(self):
        for selection in self.cards:
            rank = get_rank(Deck(*selection))
            if selection is self.straight_flush_cards:
                self.assertEqual(rank, Rank.STRAIGHT_FLUSH)
            else:
                print("NO HERE")


if __name__ == "__main__":
    unittest.main()