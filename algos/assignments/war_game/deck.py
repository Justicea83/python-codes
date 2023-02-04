from .card import Card
from . import suits, values
import random


class Deck:
    def __init__(self):

        self.all_cards = []

        for suit in suits:
            for rank in values:
                self.all_cards.append(
                    Card(suit, rank)
                )

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop()


if __name__ == '__main__':
    from doctest import testmod

    testmod()
    deck = Deck()
    deck.shuffle()
    print(deck.deal_one())
