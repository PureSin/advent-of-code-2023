from functools import total_ordering
from collections import Counter

card_values = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]

@total_ordering
class Hand:
    def __init__(self, l):
        values = l.split()
        self.hand = values[0]
        self.bid = int(values[1])
        self.counter = Counter(self.hand)

    def __str__(self) -> str:
        return f"{self.hand} {self.bid}"
    
    # we want higher rank to be larger value for more, so rank is increases    
    def __eq__(self, other):
        # TODO: maybe need to sort
        return self.counter == other.counter
    
    def smaller_first_char(self, other):
        for i in range(5):
            self_value = card_values.index(self.hand[i])
            other_value = card_values.index(other.hand[i])
            if self_value < other_value:
                return True
            elif self_value > other_value:
                return False
        return False
    
    def __lt__(self, other):
        i = 0
        self_commons = self.counter.most_common()
        other_commons = other.counter.most_common()
        if self_commons[i][1] == other_commons[i][1]: # check rank first
            # if rank is 3 then we need to check if full house
            if self_commons[i][1] == 3:
                if self_commons[1][1] == other_commons[1][1]:
                    # both full houses check strings
                    return self.smaller_first_char(other)
                return self_commons[1][1] < other_commons[1][1]
            return self.smaller_first_char(other)      
        return self_commons[i][1] < other_commons[i][1]

def calc_total_winnings(input_file):
    with open(input_file) as f:
        # parse everything
        hands = list(map(lambda l: Hand(l), f))
        hands.sort()
        for h in hands:
            print(h)
        # sort the cards
        # calculate the winnings base on order 
        winnings = 0
        for i in range(len(hands)):
            winnings += (i+1) * hands[i].bid
        print(winnings)
        
if __name__ == "__main__":
    calc_total_winnings("7_input.txt")
    # a = Hand("KKKK6 158")
    # b = Hand("5KKKK 158")
    # c = Hand("JJJJJ 158")
    # d = Hand("QQQ5Q 943")
    # l = [a, b, c, d]
    # l.sort()
    # print(a > b)
    # for h in l:
    #     print(h)