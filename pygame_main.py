"""Dependency with pygame required (run 'pip install -r requirements.txt')"""

from game import BankGameEngine
from pygame_ui import PygameUI

CARDS_TO_DEAL = 15 #modify to increase or decrease length of game

def main():
    ui = PygameUI(CARDS_TO_DEAL)
    engine = BankGameEngine(ui, CARDS_TO_DEAL)
    engine.run()

if __name__ == "__main__":
    main()
