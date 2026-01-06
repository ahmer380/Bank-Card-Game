import os

from card import Card
from ui import GameUI, GameAction

class CLI(GameUI):
    def display_welcome(self) -> None:
        print_title("Welcome to Bank!")
        print("Rules:")
        print("  - Predict if the next card is LOWER (L) or HIGHER (H)")
        print("  - Correct predictions DOUBLE your bank!")
        print("  - Wrong predictions reset your bank to 0.")
        print("  - Bank (B) at any time to lock in your score.")
        print("  - Leftover banked points are automatically added to your total score at the end.")
        print(f"  - This deck contains {self.cards_to_deal} cards in total, beat your high score!\n")
        _ = input("Press Enter to start the game... ")
    
    def display_game_state(self, current_card, cards_dealt, bank_score, total_score):
        self.clear_screen()
        print_title(f"Card {cards_dealt} / {self.cards_to_deal}")
        print(f"Current Card: {current_card} (Value: {current_card.value})")
        print(f"Bank Score: {bank_score}")
        print(f"Total Score: {total_score}")

    def get_action(self) -> GameAction:
        while True:
            print("\nWhat's your move?")
            print("  [L]ower - Next card is lower")
            print("  [H]igher - Next card is higher")
            print("  [B]ank! - Lock in your bank score")
            
            choice = input("\nEnter L, H, or B: ").strip().upper()
            
            if choice == 'L':
                return GameAction.LOWER
            elif choice == 'H':
                return GameAction.HIGHER
            elif choice == 'B':
                return GameAction.BANK
            else:
                self.handle_error("Invalid input. Please enter L, H, or B.")
    
    def display_bank_action_outcome(self, amount_banked: int) -> None:
        if amount_banked == 0:
            print("\nBANKED! But your bank was 0, so no points added...")
        else:
            print(f"\nBANKED! Added {amount_banked} to your total score!")
            print(f"Bank reset to 0")
        _ = input("\nPress Enter to continue... ")

    def display_prediction_action_outcome(self, prediction: GameAction, is_correct: bool, current_card: Card, next_card: Card) -> None:
        if is_correct:
            print(f"\nCORRECT! You predicted {prediction.value}!")
            print(f"   {current_card} --> {next_card}")
            print(f"   Bank doubled!  ")
        else:
            print(f"\nWRONG! You predicted {prediction.value}.")
            print(f"   {current_card} --> {next_card}")
            print(f"   Bank reset to 0")

        _ = input("\nPress Enter to continue... ")

    def display_game_over(self, final_score: int, new_high_score: bool) -> None:
        self.clear_screen()
        print_title("Game Over!")
        print(f"Your Final Score: {final_score}")
        
        if new_high_score:
            print_title("New High Score!")

    def ask_play_again(self) -> bool:
        while True:
            choice = input("\nPlay again? (Y/N): ").strip().upper()
            if choice == 'Y':
                return True
            elif choice == 'N':
                print("\nThanks for playing Bank! Goodbye! \n")
                return False
            else:
                self.handle_error("Invalid input. Please enter Y or N.")
    
    def handle_error(self, message: str) -> None:
        print(f"\nError: {message}\n")

    def clear_screen(self) -> None:
        os.system('cls' if os.name == 'nt' else 'clear')

def print_title(string: str) -> None:
    print("\n" + "=" * 60)
    print(string.center(60))
    print("=" * 60 + "\n")