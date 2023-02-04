from . import values


class Card:
    def __init__(self, suit, rank):
        if rank not in values:
            raise ValueError('Please enter a correct rank')

        self.suit = suit
        self.rank = rank
        self.value = values[rank]

    def __str__(self):
        return f'rank: {self.rank}, suit: {self.suit}, value: {self.value}'


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    two_hearts = Card('Hearts', 'Two')

    print(two_hearts)
