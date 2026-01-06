from enum import Enum

class Suit(Enum):
    HEARTS = "Hearts"
    DIAMONDS = "Diamonds"
    CLUBS = "Clubs"
    SPADES = "Spades"

class Rank(Enum):
    TWO = (2, "Two")
    THREE = (3, "Three")
    FOUR = (4, "Four")
    FIVE = (5, "Five")
    SIX = (6, "Six")
    SEVEN = (7, "Seven")
    EIGHT = (8, "Eight")
    NINE = (9, "Nine")
    TEN = (10, "Ten")
    JACK = (11, "Jack")
    QUEEN = (12, "Queen")
    KING = (13, "King")
    ACE = (14, "Ace")

    @property
    def numeric_value(self) -> int:
        return self._value_[0]

    @property
    def symbol(self) -> str:
        return self._value_[1]

class Card:
    def __init__(self, suit: Suit, rank: Rank):
        self.suit: Suit = suit
        self.rank: Rank = rank

    @property
    def value(self) -> int:
        return self.rank.numeric_value

    def __str__(self) -> str:
        return f"{self.rank.symbol} of {self.suit.value}"

    def __eq__(self, other) -> bool:
        return self.suit == other.suit and self.rank == other.rank

    def __lt__(self, other) -> bool:
        return self.value < other.value

    def __gt__(self, other) -> bool:
        return self.value > other.value

    def __le__(self, other) -> bool:
        return self.value <= other.value

    def __ge__(self, other) -> bool:
        return self.value >= other.value
