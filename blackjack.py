#!python3
# Written by Kody Robinson
from card import Card
import random, time

# Function to remove one card from playing deck and add to dead pile
def hitFunc(deck, hand, ddeck):
    ddeck.append(deck.pop(0))
    hand.append(ddeck[len(ddeck) - 1])
    return hand, ddeck

# Function to determine the worth of a particular hand
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

# Function to find if a hand contains a card
def contains(hand, target):
    temp = 0
    for i in hand:
        if i.cardFace() == target:
            temp += 1
    return temp

# Function to populate a deck with 6 52-card decks
def popDeck(deck):
    for i in range(6):
        for j in range(4):
            for k in range(13):
                deck.append(Card(j, k))

# Function to add cards from dead deck to main deck and then reshuffle
def reshuffleDeck(deck, ddeck):
    for i in range(len(ddeck)):
        deck.append(ddeck.pop())
    random.shuffle(deck)

# Initializes variables for a new game
def initGame(deck):
    player = []
    dealer = []
    player.append(deck.pop(0))
    dealer.append(deck.pop(0))
    player.append(deck.pop(0))   
    return player,dealer,0,0   

# Updates hand worth and prints cards in hand    
def printCards(hand, id):
    if id == 0:
        print("----------")
        print("YOUR CARDS")
        print("----------")
        for i in hand:
            i.printCard()
        handCards = detWorth(hand)
        print(str(handCards) + " - Player")
        return handCards
    else:
        print("------------")
        print("DEALER CARDS")
        print("------------")
        for i in hand:
            i.printCard()
        handCards = detWorth(hand)
        print(str(handCards) + " - Dealer")
        return handCards
        
def main():
    points = 0
    while points == 0:
        try:
            points = int(input("How many points to start: "))
        except:
            print("Enter a valid number")
    deck = []
    popDeck(deck)
    ddeck = [] # Dead deck to contain all cards that were played

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
        while wager > points and wager > 0:
            print("Insufficient amount")
            wager = int(input("What would you like to wager: "))

        reshuffleDeck(deck,ddeck)
        player, dealer, playerCards, dealerCards = initGame(deck)
        playerCards = printCards(player,0)
        dealerCards = printCards(dealer,1)

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
            player,ddeck = hitFunc(deck, player, ddeck)
            playerCards = printCards(player,0)

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

        if playerCards > 20: # Check if hand has busted or won outside of hitting loop
            continue

        # DEALER TURN
        dealer, ddeck = hitFunc(deck, dealer, ddeck)
        dealerCards = printCards(dealer,1)
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
            dealer,ddeck = hitFunc(deck, dealer,ddeck)
            dealerCards = printCards(dealer,1)

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

if __name__ == "__main__":
    main()
