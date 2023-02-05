from assignments.war_game.card import Card


class Player:
    def __init__(self, name: str):
        self.name = name
        self.all_cards: list[Card] = []

    def remove_one(self) -> Card:
        return self.all_cards.pop(0)

    def add_cards(self, new_cards: list[Card] | Card):
        if isinstance(new_cards, list):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
        pass

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


if __name__ == '__main__':
    from doctest import testmod

    testmod()
    player = Player('Emma')
    player.add_cards(Card('A', 'Two'))
    player.add_cards(Card('A', 'Three'))
    player.add_cards(Card('A', 'Four'))
    player.add_cards([Card('A', 'Six'), Card('A', 'Seven') , Card('A', 'Eight')])
    print(len(player.all_cards))
    print(player)
    player.remove_one()
    print(len(player.all_cards))
    print(player)

