#!python3
from card import Card
import random, time


def hitFunc(deck, hand):
    hand.append(deck.pop(0))
    return hand


def detWorth(hand):
    temp = 0
    aces = 0
    for i in hand:
        if i.cardFace() == "ACE":
            aces += 1
        temp = temp + i.cardWorth()
    if temp > 21 and aces > 0:
        for i in range(aces):
            temp -= 10
    return temp


def contains(hand, target):
    temp = 0
    for i in hand:
        if i.cardFace() == target:
            temp += 1
    return temp

points = 0
while points == 0:
    try:
        points = int(input("How many points to start: "))
    except:
        print("Enter a valid number")
deck = []
for i in range(6):
    for j in range(4):
        for k in range(13):
            deck.append(Card(j, k))

game_playing = True
while game_playing:
    print(f"Points available: {points}")
    if points == 0:
        print("Game Over - Out of Points")
        break
    wager = 0
    while wager == 0:
        try:
            wager = int(input("What would you like to wager: "))
        except:
            print("Enter a valid number")
    while wager > points:
        print("Insufficient amount")
        wager = int(input("What would you like to wager: "))

    random.shuffle(deck)
    player = []
    dealer = []
    playerCards = 0
    dealerCards = 0
    player.append(deck.pop(0))
    dealer.append(deck.pop(0))
    player.append(deck.pop(0))

    print("----------")
    print("YOUR CARDS")
    print("----------")
    for i in player:
        i.printCard()
    playerCards = detWorth(player)
    print(str(playerCards) + " - Player")

    print("------------")
    print("DEALER CARDS")
    print("------------")
    for i in dealer:
        i.printCard()
    dealerCards = detWorth(dealer)
    print(str(dealerCards) + " - Dealer")

    if playerCards == 21 and dealerCards < 21:
        print("You Win")
        game_playing = bool(input("Continue?\n"))
        points = points + wager
        continue

    print("Would you like to hit?")
    is_hitting = False
    if input() == "hit":
        is_hitting = True
    while is_hitting:
        player = hitFunc(deck, player)
        playerCards = detWorth(player)
        print("----------")
        print("YOUR CARDS")
        print("----------")
        for i in player:
            i.printCard()
        print(str(playerCards) + " - Player")

        if playerCards > 21:
            print("You Lose")
            game_playing = bool(input("Continue?\n"))
            points = points - wager
            break
        elif playerCards == 21:
            print("You Win")
            game_playing = bool(input("Continue?\n"))
            points = points + wager
            break
        print("Would you like to hit?")
        if input() == "hit":
            is_hitting = True
        else:
            is_hitting = False

    if playerCards > 20:
        continue

    # DEALER TURN
    dealer.append(deck.pop(0))

    print("------------")
    print("DEALER CARDS")
    print("------------")
    for i in dealer:
        i.printCard()
    dealerCards = detWorth(dealer)
    print(str(dealerCards) + " - Dealer")
    time.sleep(1)

    if dealerCards > playerCards and (dealerCards > 17 or dealerCards == 17) and dealerCards < 22:
        print("------------")
        print(str(playerCards) + " - Player")
        print(str(dealerCards) + " - Dealer")
        print("You Lose")
        game_playing = bool(input("Continue?\n"))
        points = points - wager
        continue

    while dealerCards < 17:
        dealer = hitFunc(deck, dealer)
        dealerCards = detWorth(dealer)
        print("------------")
        print("DEALER CARDS")
        print("------------")
        for i in dealer:
            i.printCard()
        print(str(dealerCards) + " - Dealer")

        if dealerCards > 21:
            print("------------")
            print(str(playerCards) + " - Player")
            print(str(dealerCards) + " - Dealer")
            print("You Win")
            game_playing = bool(input("Continue?\n"))
            points = points + wager

        elif (dealerCards > 17 or dealerCards == 17) and dealerCards > playerCards:
            print("------------")
            print(str(playerCards) + " - Player")
            print(str(dealerCards) + " - Dealer")
            print("You Lose")
            game_playing = bool(input("Continue?\n"))
            points = points - wager

        elif dealerCards == 21 and not playerCards == 21:
            print("------------")
            print(str(playerCards) + " - Player")
            print(str(dealerCards) + " - Dealer")
            print("You Lose")
            game_playing = bool(input("Continue?\n"))
            points = points - wager
        time.sleep(1)

    else:
        if playerCards > dealerCards and playerCards < 22:
            print("------------")
            print(str(playerCards) + " - Player")
            print(str(dealerCards) + " - Dealer")
            print("You Win")
            game_playing = bool(input("Continue?\n"))
            points = points + wager
    if dealerCards == playerCards:
        print("------------")
        print(str(playerCards) + " - Player")
        print(str(dealerCards) + " - Dealer")
        print("Tie")
        flag = bool(input("Continue?\n"))
