from abc import ABC, abstractmethod
from enum import Enum

from card import Card

class GameAction(Enum):
    LOWER = "Lower"
    HIGHER = "Higher"
    BANK = "Bank!"

class GameUI(ABC):
    def __init__(self, cards_to_deal: int):
        self.cards_to_deal = cards_to_deal

    @abstractmethod
    def welcome_user(self) -> None:
        pass

    @abstractmethod
    def get_action_from_game_state(self, current_card: Card, cards_dealt: int, bank_score: int, total_score: int) -> GameAction:
        pass

    @abstractmethod
    def display_bank_action_outcome(self, amount_banked: int) -> None:
        pass
    
    @abstractmethod
    def display_prediction_action_outcome(self, prediction: GameAction, is_correct: bool, current_card: Card, next_card: Card) -> None:
        pass

    @abstractmethod
    def get_user_play_again_from_game_over(self, final_score: int, new_high_score: bool) -> bool:
        pass
