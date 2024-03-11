from player import Player
from deck import Deck

class Bot(Player):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def receive_table_info(self, number_of_players, pot, flop):
        super().receive_table_info(number_of_players, pot, flop)

    def get_probability_of_win(self):
        pass
    #     deck = Deck()
    #     removees = self.hand + self.table_info.flop
    #     deck.remove(removees)
    #     flops = self.get_possible_flops(self.table_info.flop, deck)

    # def get_possible_flops(self, current_flop, d):
    #     get possible
    #     flop = current_flop


        


    def place_bet(self, minimum):
        # self.get_probability_of_win()
            




        print("Betting (to match: {}, \"f\" to fold)".format(minimum))
        while True:
            bet_size = input("Place Bet: ")
            
            if bet_size == "f":
                return "f"
            try:
                i = int(bet_size)
                valid = True
            except:
                valid = False
            if valid:
                if i <= self.balance and i >= minimum:
                    self.reduce_balance(i)
                    return i
                else:
                    print("bet out of permitted range")
            else:
                print("invalid")