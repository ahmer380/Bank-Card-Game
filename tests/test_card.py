import unittest

from src.card import Card, Suit, Rank

class TestCard(unittest.TestCase):
    def setUp(self):
        self.card_2_hearts = Card(Suit.HEARTS, Rank.TWO)
        self.card_ace_spades = Card(Suit.SPADES, Rank.ACE)
        self.card_king_diamonds = Card(Suit.DIAMONDS, Rank.KING)

    def test_card_value(self):
        self.assertEqual(self.card_2_hearts.value, 2)
        self.assertEqual(self.card_ace_spades.value, 14)
        self.assertEqual(self.card_king_diamonds.value, 13)

    def test_card_string_representation(self):
        self.assertEqual(str(self.card_2_hearts), "Two of Hearts")
        self.assertEqual(str(self.card_ace_spades), "Ace of Spades")
        self.assertEqual(str(self.card_king_diamonds), "King of Diamonds")

    def test_card_equality(self):
        card_2_hearts_duplicate = Card(Suit.HEARTS, Rank.TWO)
        self.assertEqual(self.card_2_hearts, card_2_hearts_duplicate)
        self.assertNotEqual(self.card_2_hearts, self.card_ace_spades)

    def test_card_less_than(self):
        self.assertTrue(self.card_2_hearts < self.card_king_diamonds)
        self.assertTrue(self.card_king_diamonds < self.card_ace_spades)
        self.assertFalse(self.card_ace_spades < self.card_2_hearts)

    def test_card_greater_than(self):
        self.assertTrue(self.card_ace_spades > self.card_2_hearts)
        self.assertTrue(self.card_king_diamonds > self.card_2_hearts)
        self.assertFalse(self.card_2_hearts > self.card_ace_spades)

    def test_card_less_than_or_equal(self):
        card_king_diamonds_duplicate = Card(Suit.CLUBS, Rank.KING)
        self.assertTrue(self.card_2_hearts <= self.card_king_diamonds)
        self.assertTrue(self.card_king_diamonds <= card_king_diamonds_duplicate)
        self.assertFalse(self.card_ace_spades <= self.card_2_hearts)

    def test_card_greater_than_or_equal(self):
        card_king_diamonds_duplicate = Card(Suit.CLUBS, Rank.KING)
        self.assertTrue(self.card_ace_spades >= self.card_king_diamonds)
        self.assertTrue(self.card_king_diamonds >= card_king_diamonds_duplicate)
        self.assertFalse(self.card_2_hearts >= self.card_ace_spades)

if __name__ == '__main__':
    unittest.main()
