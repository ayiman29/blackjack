import random
cards_global = {'A': 4, 'K': 4, 'Q': 4, 'J': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4, '10': 4}
cards = cards_global
def pick(cards):
    total = sum(list(cards.values()))
    if total < 39:
        reshuffle(cards)
        total = sum(list(cards.values()))
    value = random.randint(1, total)
    sumx = 0
    idx = 0
    while sumx <= total:
        sumx += cards[list(cards.keys())[idx]]
        if value <= sumx:
            cards[list(cards.keys())[idx]] -= 1
            return list(cards.keys())[idx]
        idx += 1
def reshuffle(cards):
    for k in cards:
        cards[k] = cards_global[k]
