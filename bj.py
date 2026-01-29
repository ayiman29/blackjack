import random
from time import sleep
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


def game(bet, cards = cards):
    player = []
    dealer = []
    player_score = 0
    dealer_score = 0
    print(f"Hello! You have placed a bet of {bet}$. Now, the dealer is picking your cards")
    player.append(pick(cards))
    player.append(pick(cards))
    print()
    print("Your cards are:", player)
    print()
    print("Now, the dealer is picking his cards")
    dealer.append(pick(cards))
    dealer.append(pick(cards))
    print()
    print("The dealer's first card is", dealer[0])
    flag = "H"
    while flag != "S":
        player_score = 0
        for i in player:
            if i == "A":
                player_score += 11
                A = True
            elif i == "K" or i == "Q" or i == "J":
                player_score += 10
            else:
                player_score += int(i)
        A = player.count("A")
        if player_score > 21 and A > 0:
                for i in range(A):
                    player_score -= 10
                    if player_score <= 21:
                        break
        if player_score > 21:
            return f"You are busted... You have lost {bet}$ Better luck next time!"
        elif player_score == 21:
            return f"You have WON!!! You have won {bet}$"
        print("Your score:", player_score)
        flag = input("Type (H) to Hit and (S) to Stand: ").upper()
        if flag == "H":
            player.append(pick(cards))
            print("Your cards are:", player)
    
    while True:
        dealer_score = 0
        print("Dealer's cards:", dealer)
        sleep(1)
        for i in dealer:
            if i == "A":
                dealer_score += 11
            elif i == "K" or i == "Q" or i == "J":
                dealer_score += 10
            else:
                dealer_score += int(i)
        A = dealer.count("A")
        while dealer_score > 21 and A > 0:
            dealer_score -= 10
            A -= 1
            
        print("Dealer Score:", dealer_score)
        if dealer_score >= 17:
            break
        dealer.append(pick(cards))

print(game(100000))

