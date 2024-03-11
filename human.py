from player import Player
class Human(Player):
    def __init__(self, name, balance):
        super().__init__(name, balance)

    def place_bet(self, minimum):
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