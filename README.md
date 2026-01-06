# Bank! - A 1P Card Game
Undertaking this project brought back many fond memories for the [Chess A.I Game](https://github.com/ahmer380/Chess-A.I-Game) built during my A-Levels! Bank! is a single-player card game that blends the classic Higher/Lower prediction mechanic with strategic banking elements inspired by the TV show *The Weakest Link*. The game challenges you to build the largest fortune while navigating the tension between greed and security.

<img width="1120" height="778" alt="Bank! Gameplay Screenshot" src="https://github.com/user-attachments/assets/89e6c3e9-e789-44a7-84ba-fddc6d37c64b"/>

## The Rules
- **Start**: Begin with an initial bankroll of 0 and draw cards one by one from a standard deck.
- **Predict**: Before each card is revealed, guess whether it will be higher or lower than the current card.
- **Earn**: Receive money for correct predictions, longer streaks mean bigger rewards!
- **Bank**: At any point, secure your current winnings by "banking" them into your account.
- **Risk**: An incorrect prediction costs you all unbacked winnings, resetting your streak.
- **Win**: Maximize your total banked funds by the end of the deck in order to achieve a new high score!

## Setup
This project utilises object-oriented design principles with an abstract UI layer, allowing both CLI and Pygame interfaces to share core game logic. This use of the **Strategy pattern** enables seamless extensibility: adding new interfaces requires no changes to the game engine itself. Card, deck, and game mechanics are modularised into separate components, ensuring clean separation of concerns.

### CLI
Play via the terminal with a straightforward text-based interface:
```bash
python cli_main.py
```

### GUI via Pygame
Play via the 2D graphical-based interface (Pygame dependency required):
```bash
pip install -r requirements.txt
python pygame_main.py
```

## Recommendations for extending the game
- **Leaderboards**: Track high scores and personal bests with persistent storage
- **Multiplayer Mode**: Compete against friends in real-time or turn-based matches
- **Strategy Hints**: Receive suggestions on optimal plays based on remaining cards
