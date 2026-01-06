import random

from card import Card, Suit, Rank

class Deck:
    def __init__(self):
        self.cards = []
        self.reset()

    def initialize_deck(self) -> None:
        self.cards = []
        for suit in Suit:
            for rank in Rank:
                self.cards.append(Card(suit, rank))

    def shuffle(self) -> None: #inspired by the Fisher-Yates shuffle algorithm https://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
        for i in range(len(self.cards) - 1, 0, -1):
            j = random.randint(0, i)
            self.cards[i], self.cards[j] = self.cards[j], self.cards[i]

    def deal(self) -> Card:
        if not self.cards:
            raise IndexError("Cannot deal from an empty deck")
        return self.cards.pop()

    def reset(self) -> None:
        self.initialize_deck()
        self.shuffle()
