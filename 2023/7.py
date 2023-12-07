import re
import functools
file = open('7.txt', 'r')
lines = file.readlines()

labels = ["A", "K", "Q", "J", "T", "9", "8", "7", "6", "5", "4", "3", "2"]
types = ["Five of a kind", "Four of a kind", "Full house", "Three of a kind", "Two pair", "One pair", "High card"]


def get_type(hand):
    counts = []
    for label in labels:
        counts.append(hand["cards"].count(label))
    #print(f"-- counts: {counts}")
    if 5 in counts:
        return "Five of a kind"
    elif 4 in counts:
        return "Four of a kind"
    elif 3 in counts and 2 in counts:
        return "Full house"
    elif 3 in counts:
        return "Three of a kind"
    elif counts.count(2) == 2:
        return "Two pair"
    elif 2 in counts:
        return "One pair"
    else:
        return "High card"


def get_strength(first, second):
    first_type = get_type(first)
    second_type = get_type(second)
    if types.index(first_type) < types.index(second_type):
        return 1
    elif types.index(first_type) > types.index(second_type):
        return -1
    else:
        for first_card, second_card in zip(first["cards"], second["cards"]):
            if labels.index(first_card) < labels.index(second_card):
                return 1
            elif labels.index(first_card) > labels.index(second_card):
                return -1


hands = []
for line in lines:
    cards, bid = line.split(" ")
    hand = {"cards": cards, "bid": int(bid)}
    hands.append(hand)
    print(f"Type of {cards}: {get_type(hand)}")

hands = sorted(hands, key=functools.cmp_to_key(get_strength))
print(f"Sorted {hands}")
total = 0
for rank, hand in enumerate(hands, 1):
    total += rank * hand["bid"]
print(f"Solution {total}")
