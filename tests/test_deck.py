import unittest

from src.deck import Deck
from src.card import Card

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()

    def test_deck_contents(self):
        self.assertEqual(len(self.deck.cards), 52)

        card_strings = [str(card) for card in self.deck.cards]
        self.assertEqual(len(card_strings), len(set(card_strings))) #ensure all cards are unique

    def test_shuffle_maintains_all_cards(self):
        original_cards = sorted([str(card) for card in self.deck.cards])
        self.deck.shuffle()
        shuffled_cards = sorted([str(card) for card in self.deck.cards])
        self.assertEqual(original_cards, shuffled_cards)

    def test_deal_removes_card_from_deck(self):
        initial_count = len(self.deck.cards)
        dealt_card = self.deck.deal()
        self.assertIsInstance(dealt_card, Card)
        self.assertEqual(len(self.deck.cards), initial_count - 1)

    def test_deal_removes_last_card(self):
        last_card_in_deck = self.deck.cards[-1]
        dealt_card = self.deck.deal()
        self.assertEqual(last_card_in_deck, dealt_card)
    
    def test_deal_from_empty_deck_raises_error(self):
        self.deck.cards = []
        with self.assertRaises(IndexError):
            self.deck.deal()

if __name__ == '__main__':
    unittest.main()
