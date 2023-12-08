from itertools import groupby
from pprint import pprint
ratings = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "J": 10,
    "T": 9,
    "9": 8,
    "8": 7,
    "7": 6,
    "6": 5,
    "5": 4,
    "4": 3,
    "3": 2,
    "2": 1,
}


def is_tris(hand):
    card = set(hand)
    for c in card:
        if hand.count(c) == 3:
            return True
    return False


def equal_cart_to_n(hand, n):
    card = set(hand)
    for c in card:
        if hand.count(c) == n:
            return True
    return False


def all_equal(iterable):
    g = groupby(iterable)
    return next(g, True) and not next(g, False)


def get_card_kind(hand):
    """
    KIND:
        7: SUPER POKER -> diff = 0
        6: POKER -> diff = 2
        5: FULL -> diff = 2
        4: TRIS -> diff 3
        3: DOPPIA COPPIA -> diff 3
        2: COPPIA -> 4
        1: CARTA ALTA -> 5
    """
    diff_card = len(set(hand))
    if diff_card == 1:
        if all_equal(hand):
            diff_card = 0
    match diff_card:
        case 0:
            return 7
        case 2:
            if equal_cart_to_n(hand, n=4):
                return 6
            return 5
        case 3:
            if equal_cart_to_n(hand, n=3):
                return 4
            return 3
        case 4:
            return 2
        case 5:
            return 1


def is_strongest(h1, h2):
    for index, v in enumerate(h1):
        if ratings[h1[index]] == ratings[h2[index]]:
            continue
        return ratings[h1[index]] > ratings[h2[index]]


def insert_at_pos(hand, bid, kind, deck):
    for index, elem in enumerate(deck[kind]):
        if is_strongest(hand, elem['c']):
            deck[kind].insert(index, {"c": hand, "bid": bid})
            return
    deck[kind].append({"c": hand, "bid": bid})

deck = {
    7: [],
    6: [],
    5: [],
    4: [],
    3: [],
    2: [],
    1: []
}
total_card = 0
with open("input.txt") as f:
    for line in f:
        total_card += 1
        hand = list(line.split(" ")[0])
        bid = int("".join([x for x in line.split(" ")[1] if x != ""]))
        kind = get_card_kind(hand)
        if len(deck[kind]) == 0:
            deck[kind].append({"c": hand, "bid": bid})
        else:
            insert_at_pos(hand, bid, kind, deck)

print(total_card)

pprint(deck)

rank = total_card
total = 0
for x in range(7,0, -1):
    print(len(deck[x]))
    for elem in deck[x]:
        total += (elem['bid'] * rank)
        rank -= 1

print(total)


def get_card_kind_with_joker(hand):
    """
    KIND:
        7: SUPER POKER -> diff = 0
        6: POKER -> diff = 2
        5: FULL -> diff = 2
        4: TRIS -> diff 3
        3: DOPPIA COPPIA -> diff 3
        2: COPPIA -> 4
        1: CARTA ALTA -> 5
    """
    if "J" not in hand:
        return get_card_kind(hand)

    total_j = hand.count("J")
    hand = list(filter(lambda a: a!= "J", hand))
    diff_card = len(set(hand))
    if diff_card == 1:
        if all_equal(hand):
            return 7

    tmp_dict = {}
    for c in hand:
        if c in tmp_dict.keys():
            tmp_dict[c] += 1
        else:
            tmp_dict[c] = 1

    if len(tmp_dict) == 0:
        return get_card_kind(hand)
    high_card = max(tmp_dict, key=tmp_dict.get)
    new_hand = hand + [high_card for x in range(total_j)]
    return get_card_kind(new_hand)




print("PART 2")
ratings = {
    "A": 13,
    "K": 12,
    "Q": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
    "J": 1
}

deck = {
    7: [],
    6: [],
    5: [],
    4: [],
    3: [],
    2: [],
    1: []
}
total_card = 0
with open("input.txt") as f:
    for line in f:
        total_card += 1
        hand = list(line.split(" ")[0])
        bid = int("".join([x for x in line.split(" ")[1] if x != ""]))
        kind = get_card_kind_with_joker(hand)
        if len(deck[kind]) == 0:
            deck[kind].append({"c": hand, "bid": bid})
        else:
            insert_at_pos(hand, bid, kind, deck)


print(total_card)

pprint(deck)

rank = total_card
total = 0
for x in range(7,0, -1):
    print(len(deck[x]))
    for elem in deck[x]:
        total += (elem['bid'] * rank)
        rank -= 1

print(total)