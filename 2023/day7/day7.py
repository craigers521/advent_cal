from collections import defaultdict 

class Hand:
    card_order = {"2": 1, "3": 2, "4": 3, "5": 4, "6": 5, "7": 6, "8": 7, "9": 8, "T": 9, "J": 10, "Q": 11, "K": 12, "A": 13}

    def __init__(self,card_tup):
        self.hand = card_tup[0]
        self.bid = card_tup[1]
        self.rank = self.find_rank()
    
    def __repr__(self):
        rep = f"Hand: {self.hand} Bid: {self.bid} Rank: {self.rank}"
        return rep
    
    def find_rank(self):
        score = self.base_score()
        if self.check_five(): 
            score += 1200000000
            return score
        if self.check_four(): 
            score += 1000000000
            return score
        if self.check_house(): 
            score += 800000000
            return score
        if self.check_three(): 
            score += 600000000
            return score
        if self.check_two(): 
            score += 400000000
            return score
        if self.check_one(): 
            score += 200000000
            return score
        return score
    
    def check_five(self):
        card_counts = defaultdict(int)
        for card in self.hand:
            card_counts[card] += 1
        if sorted(card_counts.values()) == [5]:
            return True
        return False
    
    def check_four(self):
        card_counts = defaultdict(int)
        for card in self.hand:
            card_counts[card] += 1
        if sorted(card_counts.values()) == [1,4]:
            return True
        else: 
            return False

    def check_house(self):
        card_counts = defaultdict(int)
        for card in self.hand:
            card_counts[card] += 1
        if sorted(card_counts.values()) == [2,3]:
            return True
        else:
            return False

    def check_three(self):
        card_counts = defaultdict(int)
        for card in self.hand:
            card_counts[card] += 1
        if set(card_counts.values()) == set([3,1]):
            return True
        else:
            return False

    def check_two(self):
        card_counts = defaultdict(int)
        for card in self.hand:
            card_counts[card] += 1
        if sorted(card_counts.values()) == [1,2,2]:
            return True
        else:
            return False

    def check_one(self):
        card_counts = defaultdict(int)
        for card in self.hand:
            card_counts[card] += 1
        if 2 in card_counts.values():
            return True
        else:
            return False

    def base_score(self):
        x=4
        value = 0
        for card in self.hand:
            value += self.card_order[card]*50**x
            x -= 1
        return value


def read_input(filename):
    lines = []
    with open(filename) as file:
        for line in file:
            lines.append(line.rstrip())
    return lines

def make_hands(lines):
    card_tups = [line.split() for line in lines]
    card_tups = [[x[0],int(x[1])] for x in card_tups]
    hands = [Hand(x) for x in card_tups]
    return hands


def card_sort(hands):
    for i in range(1,len(hands)):
        key = hands[i]
        j = i-1
        while j >= 0 and key.rank < hands[j].rank:
            hands[j+1] = hands[j]
            j -= 1
        hands[j+1] = key
    return hands

def find_winnings(hands):
    winnings = 0
    for i,hand in enumerate(hands, 1):
        winnings += hand.bid * i
    return winnings




def main():
    lines = read_input("input.txt")
    hands = make_hands(lines)
    #for hand in hands: print(repr(hand))
    #print('\n')
    sorted_hands = card_sort(hands)
    #for hand in sorted_hands: print(repr(hand))
    p1 = find_winnings(sorted_hands)
    print(p1)

    

if __name__ == "__main__":
    main()