from card import Card
from deck import Deck
from ui import GameUI, GameAction

class BankGameEngine:
    def __init__(self, ui: GameUI, cards_to_deal: int):
        self.ui = ui
        self.cards_to_deal = cards_to_deal
        self.deck = Deck()
        self.high_score = 0

    def run(self) -> None:
        self.ui.welcome_user()

        while True:
            self.play_game()
            new_high_score = self.update_high_score()
            user_play_again = self.ui.get_user_play_again_from_game_over(self.total_score, new_high_score)

            if not user_play_again:
                break

    def play_game(self) -> None:
        self.reset_game_state()

        while self.cards_dealt <= self.cards_to_deal:
            action = self.ui.get_action_from_game_state(self.current_card, self.cards_dealt, self.bank_score, self.total_score)

            if action == GameAction.BANK:
                self.perform_bank_action()
            else: #prediction_action = HIGHER or LOWER
                self.perform_prediction_action(action)
        
        self.total_score += self.bank_score

    def reset_game_state(self) -> None:
        self.deck.reset()
        self.current_card = self.deck.deal()
        self.cards_dealt = 1
        self.bank_score = 0
        self.total_score = 0

    def perform_bank_action(self) -> None:
        self.total_score += self.bank_score
        self.ui.display_bank_action_outcome(self.bank_score)
        self.bank_score = 0

    def perform_prediction_action(self, prediction: GameAction) -> None:
        next_card = self.deck.deal()
        self.cards_dealt += 1
        is_correct = self.check_prediction(prediction, self.current_card, next_card)

        if is_correct:
            self.increment_bank_score()
        else:
            self.bank_score = 0

        self.ui.display_prediction_action_outcome(prediction, is_correct, self.current_card, next_card)
        self.current_card = next_card

    def check_prediction(self, prediction: GameAction, current_card: Card, next_card: Card) -> bool:
        if prediction == GameAction.LOWER:
            return next_card.value <= current_card.value
        elif prediction == GameAction.HIGHER:
            return next_card.value >= current_card.value
        
        return False

    def increment_bank_score(self) -> None:
        if self.bank_score == 0:
            self.bank_score = 1
        else:
            self.bank_score *= 2

    def update_high_score(self) -> bool:
        if self.total_score > self.high_score:
            self.high_score = self.total_score
            return True
        
        return False