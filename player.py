from sept import Sept

class TableInfo:
    def __init__(self, num, pot, flop) -> None:
        self.num = num
        self.pot = pot
        self.flop = flop
        pass

class Player:
    def __init__(self, name, balance):
        self.name = name
        self.hand = []
        self.balance = balance
        pass

    def reset(self):
        self.hand = []
        self.quint = []
        self.quint_value = 0

    def find_quint(self, flop):
        sept = Sept(self.hand, flop)
        sept.get_best_quint()
        self.quint = sept.best_quint
        self.quint_value = sept.value
        print("{}: {} ({})".format(self.name, self.quint, self.quint_value))

    def get_balance(self):
        return self.balance

    def give_card(self, card):
        self.hand.append(card)

    def reduce_balance(self, quantity):
        self.balance -= quantity

    def increase_balance(self, quantity):
        self.balance += quantity

    def place_bet(self, minimum):
        pass

    def receive_table_info(self, number_of_players, pot, flop):
        self.table_info = TableInfo(number_of_players, pot, flop)

            




    def __repr__(self):
        str = '{}'.format(self.name)
        
        return self.name

