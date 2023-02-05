from assignments.war_game.deck import Deck
from assignments.war_game.player import Player


class Game:
    def __init__(self):
        self.player_one = Player('One')
        self.player_two = Player('Two')

        self.new_deck = Deck()
        self.new_deck.shuffle()

        for _ in range(26):
            self.player_one.add_cards(self.new_deck.deal_one())
            self.player_two.add_cards(self.new_deck.deal_one())

        self.game_one = True
        self.round_num = 0

    def play(self):
        while self.game_one:
            self.round_num += 1
            print(f'Round {self.round_num}')

            if len(self.player_one.all_cards) == 0:
                print('Player One, out of cards! Player Two Wins!')
                self.game_one = False
                break

            if len(self.player_two.all_cards) == 0:
                print('Player Two, out of cards! Player One Wins!')
                self.game_one = False
                break

            player_one_cards = [self.player_one.remove_one()]
            player_two_cards = [self.player_two.remove_one()]

            at_war = True

            while at_war:
                if player_one_cards[-1].value > player_two_cards[-1].value:
                    self.player_one.add_cards(player_one_cards)
                    self.player_one.add_cards(player_two_cards)

                    at_war = False

                elif player_two_cards[-1].value > player_one_cards[-1].value:
                    self.player_two.add_cards(player_one_cards)
                    self.player_two.add_cards(player_two_cards)

                    at_war = False

                else:
                    print('WAR!')

                    if len(self.player_one.all_cards) < 5:
                        print('Player One cannot declare war')
                        print('PLAYER TWO WINS')

                        self.game_one = False
                        break

                    elif len(self.player_two.all_cards) < 5:
                        print('Player TWO cannot declare war')
                        print('PLAYER ONE WINS')

                        self.game_one = False
                        break

                    else:
                        for num in range(5):
                            player_one_cards.append(self.player_one.remove_one())
                            player_two_cards.append(self.player_two.remove_one())


if __name__ == '__main__':
    from doctest import testmod

    testmod()

    game = Game()
    game.play()
