import unittest

from game import BankGameEngine
from card import Card, Suit, Rank
from ui import GameAction

class TestBankGameEngine(unittest.TestCase):
    def setUp(self):
        self.engine = BankGameEngine(None, 10)

    def test_increment_bank_score_from_zero(self):
        self.engine.bank_score = 0
        self.engine.increment_bank_score()
        self.assertEqual(self.engine.bank_score, 1)

    def test_increment_bank_score_doubles(self):
        self.engine.bank_score = 8
        self.engine.increment_bank_score()
        self.assertEqual(self.engine.bank_score, 16)
        self.engine.increment_bank_score()
        self.assertEqual(self.engine.bank_score, 32)

    def test_check_prediction_higher_correct(self):
        current_card = Card(Suit.HEARTS, Rank.TWO)
        next_card = Card(Suit.HEARTS, Rank.FIVE)
        result = self.engine.check_prediction(GameAction.HIGHER, current_card, next_card)
        self.assertTrue(result)

    def test_check_prediction_higher_incorrect(self):
        current_card = Card(Suit.HEARTS, Rank.ACE)
        next_card = Card(Suit.HEARTS, Rank.TWO)
        result = self.engine.check_prediction(GameAction.HIGHER, current_card, next_card)
        self.assertFalse(result)

    def test_check_prediction_higher_equal(self):
        current_card = Card(Suit.HEARTS, Rank.FIVE)
        next_card = Card(Suit.DIAMONDS, Rank.FIVE)
        result = self.engine.check_prediction(GameAction.HIGHER, current_card, next_card)
        self.assertTrue(result)

    def test_check_prediction_lower_correct(self):
        current_card = Card(Suit.HEARTS, Rank.ACE)
        next_card = Card(Suit.HEARTS, Rank.TWO)
        result = self.engine.check_prediction(GameAction.LOWER, current_card, next_card)
        self.assertTrue(result)

    def test_check_prediction_lower_incorrect(self):
        current_card = Card(Suit.HEARTS, Rank.TWO)
        next_card = Card(Suit.HEARTS, Rank.ACE)
        result = self.engine.check_prediction(GameAction.LOWER, current_card, next_card)
        self.assertFalse(result)

    def test_check_prediction_lower_equal(self):
        current_card = Card(Suit.HEARTS, Rank.FIVE)
        next_card = Card(Suit.DIAMONDS, Rank.FIVE)
        result = self.engine.check_prediction(GameAction.LOWER, current_card, next_card)
        self.assertTrue(result)

    def test_update_high_score_new_high_score(self):
        self.engine.high_score = 0
        self.engine.total_score = 100
        result = self.engine.update_high_score()
        self.assertTrue(result)
        self.assertEqual(self.engine.high_score, 100)

    def test_update_high_score_not_new_high_score(self):
        self.engine.high_score = 100
        self.engine.total_score = 50
        result = self.engine.update_high_score()
        self.assertFalse(result)
        self.assertEqual(self.engine.high_score, 100)

    def test_update_high_score_equal_to_high_score(self):
        self.engine.high_score = 100
        self.engine.total_score = 100
        result = self.engine.update_high_score()
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main()
