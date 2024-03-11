from player import Player
from card import Card
from deck import Deck
from human import Human
from bot import Bot


class PokerGame:
    def __init__(self, players):
        self.players = players
        self.deck = []
        self.flop = []
        self.pot = 0
        self.done = False
        
    def prepare_game(self):
        self.done = False
        for player in self.players:
            player.reset()
        self.deck = Deck()
        self.deck.shuffle()

    def deal(self, quantity):
        for player in self.players:
            for i in range(quantity):
                card = self.deck.pull_card()
                player.give_card(card)

    def betting(self):
        if self.done:
            return
        highest_bet = 0
        amounts_placed = {}
        i = 0
        while i < len(self.remaining_players):
            folding = False
            player = self.remaining_players[i]
            print("{}: ${}".format(player.name, player.balance))
            print(player.hand)
            minimum = highest_bet
            player.receive_table_info(len(self.remaining_players), self.pot, self.flop)
            bet = player.place_bet(minimum)
            if bet == "f":
                print("{} folds".format(player.name))
                print("\n\n")
                folding = True
                self.remaining_players.remove(player)
                if len(self.remaining_players) == 1:
                    self.done = True
                    return
            else:
                highest_bet = max(highest_bet, bet)
                amounts_placed[player] = bet
                self.pot += bet
                print("\n\n")

            if not folding:
                i += 1

        i=0
        while True:
            folding = False            
            player = self.remaining_players[i]
            minimum = highest_bet - amounts_placed[player]
            if minimum == 0:
                break
            print("{}: ${}".format(player.name, player.balance))
            print(player.hand)
            player.receive_table_info(len(self.remaining_players), self.pot, self.flop)
            bet = player.place_bet(minimum)
            if bet == "f":
                print("{} folds".format(player.name))
                print("\n\n")
                folding == True
                self.remaining_players.remove(player)
                if len(self.remaining_players) == 1:
                    self.done = True
                    return
            else:
                amounts_placed[player] += bet
                highest_bet = max(highest_bet, amounts_placed[player])
                self.pot += bet
                print("\n\n")

            if not folding:
                i+=1

            if i >= len(self.remaining_players):
                i = 0
            
    def add_to_flop(self, quantity):
        if self.done:
            return
        for i in range(quantity):
            card = self.deck.pull_card()
            self.flop.append(card)
        print("\n")
        print("Pot: ${}".format(self.pot))
        print(self.flop)
        print("\n")

    def get_winners(self):
        if len(self.remaining_players) == 1:
            return self.remaining_players[:]
        best_players = []
        best_type_value = 0
        for player in self.remaining_players:
            player.find_quint(self.flop)
            if player.quint_value > best_type_value:
                best_type_value = player.quint_value
                best_players = []
                best_players.append(player)
            elif player.quint_value == best_type_value:
                best_players.append(player)
            else:
                pass
        remaining = []
        for i in range(5):
            if len(best_players) == 1:
                break
            best_sorting_value = 0
            for player in best_players:
                card = player.quint[i]
                sorting_value = card.get_sorting_value()
                if sorting_value > best_sorting_value:
                    best_sorting_value = sorting_value
                    remaining = []
                    remaining.append(player)
                elif sorting_value == best_sorting_value:
                    remaining.append(player)
                else:
                    pass
            best_players = remaining
        return best_players

    def score_and_reward(self):
        winners = self.get_winners()
        winnings = self.pot/len(winners)
        print("Game Over:", winners, "wins", "${}".format(winnings), "!")
        for player in winners:
            player.increase_balance(winnings)
        self.pot = 0
        self.flop = []

    def play(self):
        print("New Round:\n")
        self.prepare_game()
        self.remaining_players = self.players[:]
        # self.ante()
        self.deal(2)
        self.betting()
        self.add_to_flop(3)
        self.betting()
        self.add_to_flop(1)
        self.betting()
        self.add_to_flop(1)
        self.betting()
        self.score_and_reward()

def main():
    # letters = "abcdefg"
    # players = []
    # for chr in letters:
    #     p = Player(chr, 1000)
    #     players.append(p)
    player1 = Human("Jonas", 1000)
    player2 = Bot("Katie", 1000)
    player3 = Bot("Ricky", 1000)
    players = [player1, player2, player3]
    game = PokerGame(players)
    for i in range(50):
        game.play()


main()
