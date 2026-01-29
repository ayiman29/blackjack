import random
from time import sleep
cards_global = {'A': 4, 'K': 4, 'Q': 4, 'J': 4, '2': 4, '3': 4, '4': 4, '5': 4, '6': 4, '7': 4, '8': 4, '9': 4, '10': 4}
cards = cards_global.copy()
def pick(cards):
    total = sum(list(cards.values()))
    if total < 15: #cut-card = 15
        reshuffle(cards)
        total = sum(list(cards.values()))
    value = random.randint(1, total)
    sumx = 0
    idx = 0
    while idx < len(cards):
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
    sleep(1)
    player.append(pick(cards))
    player.append(pick(cards))
    print()
    print("Your cards are:", player)
    print()
    sleep(1)
    print("Now, the dealer is picking his cards")
    dealer.append(pick(cards))
    dealer.append(pick(cards))
    print()
    sleep(1)
    print(f"Dealer's cards are [{dealer[0]}, XX]")
    flag = "H"
    player_blackjack = False
    dealer_blackjack = False
    while flag != "S":
        player_score = 0
        for i in player:
            if i == "A":
                player_score += 11
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
            print("Your score:", score)
            return 0
        elif player_score == 21:
            print("Your Score: 21!!!!")
            
            if len(player) == 2:
                player_blackjack = True
            break
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
        if dealer_score == 21 and len(dealer) == 2:
            dealer_blackjack = True
        print("Dealer Score:", dealer_score)
        if dealer_score >= 17:
            break
        dealer.append(pick(cards))
    
    if dealer_blackjack > 21:
        return 1
    if dealer_blackjack:
        if player_blackjack:
            return 3
        else:
            return 0
    if player_blackjack:
        return 2

    elif player_score > dealer_score:
        return 1
    elif dealer_score > player_score:
        return 0
    else:
        return 3

#0 -> Dealer wins
#1 -> Player wins
#2 -> Player blackjack
#3 -> push


bet = int(input("WELCOME TO BLACKJACK!!!! PLEASE PLACE YOUR BET: "))
sleep(1)
res = game(bet)
sleep(1)
if res == 0:
    print("YOU HAVE LOST;((")
    print(f"LOST: {bet}$")
elif res == 1:
    print("YOU HAVE WON!!!")
    print(f"WON: {bet}$")
elif res == 2:
    print("$$$BLACKJACK$$$")
    print(f"WON: {bet*(1.5)}$")
else:
    print("It's a Push!")

