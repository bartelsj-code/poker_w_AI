sorting_values = {"A": 14, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "10": 10, "J": 11, "Q": 12, "K": 13}

class Card:
    def __init__(self, value, suit, card_id):
        self.value = value
        self.suit = suit
        self.sorting_value = sorting_values[self.value]
        self.id = card_id

    def copy(self):
        return Card(self.value, self.suit)

    def get_value(self):
        return self.value

    def get_sorting_value(self):
        return self.sorting_value

    def get_suit(self):
        return self.suit
    
    def __repr__(self):
        str = "{}{}".format(self.value, self.suit)
        return str
    
    def __lt__(self, other):
        return self.sorting_value < other.sorting_value


        