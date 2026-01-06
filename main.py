from game import BankGameEngine
from cli_ui import CLIUI

CARDS_TO_DEAL = 15 #modify to increase or decrease length of game

def main():
    ui = CLIUI(CARDS_TO_DEAL)
    engine = BankGameEngine(ui, CARDS_TO_DEAL)

    try:
        engine.run()
    except KeyboardInterrupt:
        ui.handle_error("\nGame interrupted. Goodbye!")

if __name__ == "__main__":
    main()
