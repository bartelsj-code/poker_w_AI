from card import Card
import random
class Deck:
    def __init__(self):
        self.values = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
        self.suits = ["C", "D", "S", "H"]
        self.cards = []
        self.generate_cards()

    def generate_cards(self):
        i = 0
        for value in self.values:
            for suit in self.suits:
                card = Card(value, suit, i)
                self.cards.append(card)
                i += 1

    def shuffle(self):
        random.shuffle(self.cards)

    def pull_card(self):
        try:
            return self.cards.pop()
        except:
            print("deck is out of cards")

    def remove(self, lst):
        lst.sort(key = lambda card:card.id)
        lst.reverse()
        for card in lst:            
            self.cards.pop(card.id)


