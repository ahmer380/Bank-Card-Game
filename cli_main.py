"""No dependency with pygame required"""

from src.game import BankGameEngine
from src.cli_ui import CLI

CARDS_TO_DEAL = 15 #modify to increase or decrease length of game

def main():
    ui = CLI(CARDS_TO_DEAL)
    engine = BankGameEngine(ui, CARDS_TO_DEAL)

    try:
        engine.run()
    except KeyboardInterrupt:
        ui.handle_error("\nGame interrupted. Goodbye!")

if __name__ == "__main__":
    main()
