import unittest
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
            Card(Suit.DIAMONDS, Value.THREE)
        ]
        self.straight_flush_cards = [
            Card(Suit.DIAMONDS, Value.KING),
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.DIAMONDS, Value.TEN),
            Card(Suit.DIAMONDS, Value.NINE),
            Card(Suit.DIAMONDS, Value.TWO),
            Card(Suit.DIAMONDS, Value.THREE)
        ]
        self.four_of_a_kind = [
            Card(Suit.DIAMONDS, Value.KING),
            Card(Suit.HEARTS, Value.KING),
            Card(Suit.SPADES, Value.KING),
            Card(Suit.CLUBS, Value.KING),
            Card(Suit.DIAMONDS, Value.NINE),
            Card(Suit.DIAMONDS, Value.TWO),
            Card(Suit.DIAMONDS, Value.THREE)
        ]
        self.full_house = [
            Card(Suit.DIAMONDS, Value.KING),
            Card(Suit.HEARTS, Value.KING),
            Card(Suit.SPADES, Value.KING),
            Card(Suit.CLUBS, Value.JACK),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.DIAMONDS, Value.TWO),
            Card(Suit.DIAMONDS, Value.THREE)
        ]
        self.flush_cards = [
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.DIAMONDS, Value.TEN),
            Card(Suit.DIAMONDS, Value.NINE),
            Card(Suit.DIAMONDS, Value.FIVE),
            Card(Suit.CLUBS, Value.TWO),
            Card(Suit.CLUBS, Value.THREE)
        ]
        self.straight_cards = [
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.CLUBS, Value.TEN),
            Card(Suit.SPADES, Value.NINE),
            Card(Suit.DIAMONDS, Value.EIGHT),
            Card(Suit.CLUBS, Value.TWO),
            Card(Suit.CLUBS, Value.THREE)
        ]
        self.three_of_a_kind_cards = [
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.CLUBS, Value.TEN),
            Card(Suit.SPADES, Value.NINE),
            Card(Suit.SPADES, Value.THREE),
            Card(Suit.DIAMONDS, Value.THREE),
            Card(Suit.CLUBS, Value.THREE)
        ]
        self.two_pairs = [
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.CLUBS, Value.TEN),
            Card(Suit.CLUBS, Value.FOUR),
            Card(Suit.SPADES, Value.FOUR),
            Card(Suit.DIAMONDS, Value.THREE),
            Card(Suit.CLUBS, Value.THREE)
        ]
        self.one_pair = [
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.CLUBS, Value.TEN),
            Card(Suit.SPADES, Value.NINE),
            Card(Suit.SPADES, Value.FOUR),
            Card(Suit.DIAMONDS, Value.THREE),
            Card(Suit.CLUBS, Value.THREE)
        ]
        self.high_card = [
            Card(Suit.DIAMONDS, Value.QUEEN),
            Card(Suit.DIAMONDS, Value.JACK),
            Card(Suit.CLUBS, Value.TEN),
            Card(Suit.SPADES, Value.NINE),
            Card(Suit.SPADES, Value.FOUR),
            Card(Suit.DIAMONDS, Value.FIVE),
            Card(Suit.CLUBS, Value.THREE)
        ]
        self.cards = [
            self.royal_flush_cards,
            self.straight_flush_cards,
            self.four_of_a_kind,
            self.full_house,
            self.flush_cards,
            self.straight_cards,
            self.three_of_a_kind_cards,
            self.two_pairs,
            self.one_pair,
            self.high_card
        ]

    def test_royal_flush(self):
        for selection in self.cards:
            rank: WinningRank = get_rank(Deck(*selection))
            if selection is self.royal_flush_cards:
                self.assertEqual(Rank.ROYAL_FLUSH, rank.rank)
            else:
                self.assertNotEqual(Rank.ROYAL_FLUSH, rank.rank)

    def test_straight_flush(self):
        for selection in self.cards:
            rank: WinningRank = get_rank(Deck(*selection))
            if selection is self.straight_flush_cards:
                self.assertEqual(Rank.STRAIGHT_FLUSH, rank.rank)
            else:
                self.assertNotEqual(Rank.STRAIGHT_FLUSH, rank.rank)

    def test_four_of_a_kind(self):
        for selection in self.cards:
            rank: WinningRank = get_rank(Deck(*selection))
            if selection is self.four_of_a_kind:
                self.assertEqual(Rank.FOUR_OF_A_KIND, rank.rank)
            else:
                self.assertNotEqual(Rank.FOUR_OF_A_KIND, rank.rank)

    def test_full_house(self):
        for selection in self.cards:
            rank: WinningRank = get_rank(Deck(*selection))
            if selection is self.full_house:
                self.assertEqual(Rank.FULL_HOUSE, rank.rank)
            else:
                self.assertNotEqual(Rank.FULL_HOUSE, rank.rank)

    def test_flush(self):
        for selection in self.cards:
            rank: WinningRank = get_rank(Deck(*selection))
            if selection is self.flush_cards:
                self.assertEqual(Rank.FLUSH, rank.rank)
            else:
                self.assertNotEqual(Rank.FLUSH, rank.rank)

    def test_straight(self):
        for selection in self.cards:
            rank: WinningRank = get_rank(Deck(*selection))
            if selection is self.straight_cards:
                self.assertEqual(Rank.STRAIGHT, rank.rank)
            else:
                self.assertNotEqual(Rank.STRAIGHT, rank.rank)

    def test_three_of_a_kind(self):
        for selection in self.cards:
            rank: WinningRank = get_rank(Deck(*selection))
            if selection is self.three_of_a_kind_cards:
                self.assertEqual(Rank.THREE_OF_A_KIND, rank.rank)
            else:
                self.assertNotEqual(Rank.THREE_OF_A_KIND, rank.rank)

    def test_two_pair(self):
        for selection in self.cards:
            rank: WinningRank = get_rank(Deck(*selection))
            if selection is self.two_pairs:
                self.assertEqual(Rank.TWO_PAIR, rank.rank)
            else:
                self.assertNotEqual(Rank.TWO_PAIR, rank.rank)

    def test_one_pair(self):
        for selection in self.cards:
            rank: WinningRank = get_rank(Deck(*selection))
            if selection is self.one_pair:
                self.assertEqual(Rank.ONE_PAIR, rank.rank)
            else:
                self.assertNotEqual(Rank.ONE_PAIR, rank.rank)

    def test_high_card(self):
        for selection in self.cards:
            rank: WinningRank = get_rank(Deck(*selection))
            if selection is self.high_card:
                self.assertEqual(Rank.HIGH_CARD, rank.rank)
            else:
                self.assertNotEqual(Rank.HIGH_CARD, rank.rank)


if __name__ == "__main__":
    unittest.main()
