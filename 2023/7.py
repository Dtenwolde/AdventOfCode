from collections import defaultdict
from enum import Enum

class CardRankings(Enum):
    ACE = 13
    KING = 12
    QUEEN = 11
    TRUMP = 10
    NINE = 9
    EIGHT = 8
    SEVEN = 7
    SIX = 6
    FIVE = 5
    FOUR = 4
    THREE = 3
    TWO = 2
    JOKER = 1

    def __lt__(self, other):
        return self.value < other.value

    def __str__(self):
        return f"{self.value}"

    __repr__ = __str__

class HandRankings(Enum):
    FIVE_OF_A_KIND = 6
    FOUR_OF_A_KIND = 5
    FULL_HOUSE = 4
    THREE_OF_A_KIND = 3
    TWO_PAIR = 2
    ONE_PAIR = 1
    HIGH_CARD = 0
    UNKNOWN = -1

    def __lt__(self, other):
        return self.value < other.value

class Hand:
    def __init__(self, card_input, bid):
        self.original_card_input = card_input
        self.result = HandRankings.HIGH_CARD
        self.bid = bid
        for joker in "AKQT98765432J":
            self.cards = []
            self.jokered_card_input = card_input.replace("J", joker)

            for card in self.jokered_card_input:
                if card == "A":
                    self.cards.append(CardRankings.ACE)
                elif card == "K":
                    self.cards.append(CardRankings.KING)
                elif card == "Q":
                    self.cards.append(CardRankings.QUEEN)
                elif card == "J":
                    self.cards.append(CardRankings.JOKER)
                elif card == "T":
                    self.cards.append(CardRankings.TRUMP)
                elif card == "9":
                    self.cards.append(CardRankings.NINE)
                elif card == "8":
                    self.cards.append(CardRankings.EIGHT)
                elif card == "7":
                    self.cards.append(CardRankings.SEVEN)
                elif card == "6":
                    self.cards.append(CardRankings.SIX)
                elif card == "5":
                    self.cards.append(CardRankings.FIVE)
                elif card == "4":
                    self.cards.append(CardRankings.FOUR)
                elif card == "3":
                    self.cards.append(CardRankings.THREE)
                elif card == "2":
                    self.cards.append(CardRankings.TWO)
            new_ranking = self.check_result()
            if new_ranking > self.result:
                self.result = new_ranking
    def __str__(self):
        return f"({self.jokered_card_input}, {self.original_card_input} {self.bid}, {self.result})"

    __repr__ = __str__

    def __lt__(self, other):
        if self.result < other.result:
            return True
        elif self.result == other.result:
            if self.cards[0] < other.cards[0]:
                return True
            elif self.cards[0] > other.cards[0]:
                return False
            if self.cards[1] < other.cards[1]:
                return True
            elif self.cards[1] > other.cards[1]:
                return False
            if self.cards[2] < other.cards[2]:
                return True
            elif self.cards[2] > other.cards[2]:
                return False
            if self.cards[3] < other.cards[3]:
                return True
            elif self.cards[3] > other.cards[3]:
                return False
            if self.cards[4] < other.cards[4]:
                return True
            elif self.cards[4] > other.cards[4]:
                return False
            return False
        return False
    def check_result(self):
        if self.check_five_of_a_kind():
            return HandRankings.FIVE_OF_A_KIND
        if self.check_four_of_a_kind():
            return HandRankings.FOUR_OF_A_KIND
        if self.check_full_house():
            return HandRankings.FULL_HOUSE
        if self.check_three_of_a_kind():
            return HandRankings.THREE_OF_A_KIND
        if self.check_two_pair():
            return HandRankings.TWO_PAIR
        if self.check_one_pair():
            return HandRankings.ONE_PAIR
        return HandRankings.HIGH_CARD

    def check_five_of_a_kind(self):
        if len(set(self.cards)) == 1:
            print(f"Five of a kind {self.jokered_card_input}")
            return True
        return False

    def check_four_of_a_kind(self):
        card_dict = defaultdict(int)
        for card in self.cards:
            card_dict[card] += 1
        for k, v in card_dict.items():
            if v == 4:
                print(f"Four of a kind {self.jokered_card_input}")
                return True
        return False
    def check_full_house(self):
        sorted_cards = sorted(self.cards)
        if (len(set(sorted_cards[:3])) == 1 and len(set(sorted_cards[3:])) == 1) or \
            (len(set(sorted_cards[:2])) == 1 and len(set(sorted_cards[2:])) == 1):
            print(f"Full house {self.jokered_card_input}")
            return True
    def check_three_of_a_kind(self):
        card_dict = defaultdict(int)
        for card in self.cards:
            card_dict[card] += 1
        for k, v in card_dict.items():
            if v == 3:
                print(f"Three of a kind {self.jokered_card_input}")
                return True
        return False
    def check_two_pair(self):
        card_dict = defaultdict(int)
        for card in self.cards:
            card_dict[card] += 1
        pairs = 0
        for k, v in card_dict.items():
            if v == 2:
                pairs += 1
        if pairs == 2:
            print(f"Two pair {self.jokered_card_input}")
            return True
    def check_one_pair(self):
        card_dict = defaultdict(int)
        for card in self.cards:
            card_dict[card] += 1
        for k, v in card_dict.items():
            if v == 2:
                print(f"One pair {self.jokered_card_input}")
                return True
        return False
def main():
    input_ = open("7_input.txt").read().split("\n")
    hands = []
    for hand in input_:
        cards, bid = hand.split()
        hands.append(Hand(cards, int(bid)))
    sorted_hands = sorted(hands)
    total_ranking = 0
    for idx, hand in enumerate(sorted_hands):
        print(hand, idx + 1, (idx + 1) * hand.bid )
        total_ranking += (idx + 1) * hand.bid
    print(total_ranking)


if __name__ == "__main__":
    main()

# 2345A 1
# J345A 2
# 2345J 3
# 32T3K 5
# KK677 7
# T3Q33 11
# Q2KJJ 13
# T3T3J 17
# Q2Q2Q 19
# 2AAAA 23
# T55J5 29
# QQQJA 31
# KTJJT 34
# JJJJJ 37
# JJJJ2 41
# JAAAA 43
# 2JJJJ 53
# AAAAJ 59
# AAAAA 61