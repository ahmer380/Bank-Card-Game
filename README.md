# Bank! Card Game

A simple higher/lower card game with two UIs:
- Terminal CLI (`main.py`)
- Minimal Pygame GUI (`pygame_main.py`), mouse-only

## Quick Start

### CLI
```bash
python main.py
```

### GUI (Pygame)
Install dependency:
```bash
pip install -r requirements.txt
```
Run the GUI:
```bash
python pygame_main.py
```

## Rules
- Predict whether the next card is lower or higher.
- Correct predictions double your bank; wrong predictions reset it to 0.
- Click "Bank!" to lock in your bank and add it to the total.
- Remaining bank is added automatically at the end.

## Config
- Modify `CARDS_TO_DEAL` in `main.py` or `pygame_main.py` to change game length.
