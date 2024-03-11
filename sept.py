from card import Card
type_values = {"HC": 0, "P": 1, "2P": 2, "3K": 3, "S": 4, "F": 5, "FH": 6, "4K": 7, "SF": 8, "RF": 9}

class Sept:
    def __init__(self, hand, flop):
        self.all_cards = hand + flop
        self.all_cards.sort(reverse = True)
        self.value = 0
        self.best_quint = []

    def get_best_quint(self):
        flush = self.highest_flush(self.all_cards)
        if flush != None:
            straight_flush = self.straight_flush(self.all_cards)
            if straight_flush != None:
                royal_flush = self.royal_flush(straight_flush)
                if royal_flush != None:
                    self.value = type_values["RF"]
                    self.best_quint = royal_flush
                    return
                else:
                    self.value = type_values["SF"]
                    self.best_quint = straight_flush
                    return
        best_set, remainder = self.of_a_kinds(self.all_cards)
        if len(best_set) == 4:
            self.value = type_values["4K"]
            best_set.append(remainder[0])
            self.best_quint = best_set
            return
        second_set, second_remainder = self.of_a_kinds(remainder)
        if len(best_set) == 3 and len(second_set) == 2:
            self.value = type_values["FH"]
            self.best_quint = best_set + second_set
            return
        if flush != None:
            self.value = type_values["F"]
            self.best_quint = flush
            return
        straight = self.highest_straight(self.all_cards)
        if straight != None:
            self.value = type_values["S"]
            self.best_quint = straight
            return
        if len(best_set) == 3:
            self.value = type_values["3K"]
            self.best_quint = best_set + remainder[:2]
            return
        if len(best_set) == 2 and len(second_set) == 2:
            self.value = type_values["2P"]
            second_set.append(second_remainder[0])
            self.best_quint = best_set + second_set
            return
        if len(best_set) == 2:
            self.value = type_values["P"]
            self.best_quint = best_set + remainder[:3]
            return
              
        self.value = type_values["HC"]
        self.best_quint = self.all_cards[:5]
        return
    
    def of_a_kinds(self, cards1):
        cards = cards1[:]
        best_value = ""
        max_encounters = 0
        encounters_dict = {"A": [], "K": [], "Q": [], "J": [], "10": [], "9": [], "8": [], "7": [], "6": [], "5": [], "4": [], "3": [], "2": []}
        for card in cards:
            value = card.get_value()
            encounters_dict[value].append(card)
            if len(encounters_dict[value]) > max_encounters:
                max_encounters = len(encounters_dict[value])
                best_value = value
        best_set = encounters_dict[best_value][:]
        encounters_dict[best_value] = []
        remainder = []
        for value in encounters_dict:
            for card in encounters_dict[value]:
                remainder.append(card)
        return best_set, remainder


            
    
    def royal_flush(self, cards):
        if cards[0].get_value() == "A":
            return cards
        return None
        
    def straight_flush(self, cards1):
        suit = ""
        cards = cards1[:]
        suit_dict =  {"H": 0, "D": 0, "S": 0, "C": 0}
        for card in cards:
            suit_dict[card.get_suit()] += 1
            if suit_dict[card.get_suit()] == 3:
                suit = card.get_suit()
        new_cards = []
        for card in cards:
            if suit == card.get_suit():
                new_cards.append(card)
        quints = []
        if len(new_cards) >= 5:
            quints.append(new_cards[0:5])
        if len(new_cards) >= 6:
            quints.append(new_cards[1:6])
        if len(new_cards) == 7:
            quints.append(new_cards[2:7])
        for quint in quints:
            straight = self.highest_straight(quint)
            if straight != None:
                return straight
        return None
                
    def highest_straight(self, cards1):
        cards = cards1[:]
        partial = []
        last_value = 15
        if cards[0].get_value() == "A":
            new_ace = cards[0].copy()
            new_ace.sorting_value = 1
            cards.append(new_ace)

        remaining = len(cards)
        
        for card in cards:
            if len(partial) + remaining < 5:
                return None
            if card.get_sorting_value() == last_value - 1:
                partial.append(card)
                if len(partial) == 5:
                    return partial
            elif card.get_sorting_value() == last_value:
                pass
            else:
                partial = []
                partial.append(card)

            last_value = card.get_sorting_value()
            remaining -= 1     
        return None

    def highest_flush(self, cards):
        remaining = len(cards)-1
        best_length = 0
        best_suit = ""
        flushes = {"D": [], "C": [], "S":[], 'H':[]}
        for card in cards:
            suit = card.get_suit()
            partial = flushes[suit]
            partial.append(card)
            if best_length < len(partial):
                best_length += 1
                best_suit = suit
            if remaining + best_length < 5:
                return None
            if best_length == 5:
                return flushes[best_suit]
            remaining -= 1
        return None

    def __repr__(self):
        return str(self.all_cards)