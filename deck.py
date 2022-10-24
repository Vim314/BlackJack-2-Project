from cgi import test
from hashlib import new
import random
import numpy as np
import time
#This is THIRD Version [for github reasons]

#Testing update

#Testing yet again

#Last test

#Create deck of cards with numpy:
#dealerDeck = np.array(np.meshgrid(["Ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King"], ["Clubs", "Hearts", "Diamonds", "Spades"])).T.reshape(52,-1)

#Defining suits, ranks, and value for each rank
suits = ("Clubs", "Hearts", "Diamonds", "Spades")
ranks = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen", "King")
values = {"Ace":11, "Two":2, "Three":3, "Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10, "Jack":10, "Queen":10, "King":10}

playing = True
#busted = False

#Creating outline for each card
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return self.rank + " of " + self.suit


#Deck of Cards
class Deck:
    def __init__(self):
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit, rank))

    def __str__(self):
        fullDeck = ''
        length = 0
        for card in self.deck:
            fullDeck += '\n ' + card.__str__()
            length += 1
        print(length)
        return 'The deck has:' + fullDeck

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        card = self.deck.pop(0)
        return card


#Player hand
class Player:
    def __init__(self):
        self.hand = []
        self.value = 0
        self.aces = 0
    
    def __str__(self):
        fullHand = ""
        length = 0
        for card in self.hand:
            fullHand += "\n " + card.__str__()
            length += 1
        print("Number of Cards: ", length)
        print("Value of Hand: ", self.value)
        return "Your hand contains:" + fullHand
    
    def add_card(self, card):
        self.hand.append(card)
        self.value += values[card.rank]
        if card.rank == "Ace":
            self.aces += 1

    def fixAce(self):
        while self.value > 21 and self.aces>0:
            self.value -= 10
            self.aces -= 1
    
    def showDealerHand(self):
        print(self.hand[1])


class Chips:
    def __init__(self):
        self.total = 100
        self.bet = 0
    
    def win_bet(self):
        self.total += self.bet
    
    def lose_bet(self):
        self.total -= self.bet


def player_hit(deck, hand):
    hand.add_card(deck.deal())
    hand.fixAce

def player_busts(bustedPlayer):
    print("You Busted!")

def dealer_busts(dealer):
    print("Dealer Busted!\nYou win!")

def hit_or_stand(deck, player):
    global playing
    #global busted
    playing = True
    
    while True:
        pInput = input("Hit or Stand? ")
        pInput.lower()
        if(pInput == "hit"):
            player_hit(deck, player)

        elif(pInput == "stand"):
            print("Dealer will now play...")
            playing = False

        else:
            print("Sorry")
            continue
        break

def showSome(player, dealer):
    print("\nDealer's Hand:")
    print(" <Hidden Card> ")
    print(" ", dealer.hand[1])
    print("\nYour hand's value: ", player.value)
    print("Player's Hand:", *player.hand, sep = "\n")

def showAll(player, dealer):
    print("\nDealer's Hand:", *dealer.hand, sep = "\n")
    print("Dealer's Hand Value: ", dealer.value)
    print("\nPlayer's Hand:", *player.hand, sep = "\n")
    print("Player's Hand Value: ", player.value)

def playerWin():
    print("Congratulations, you win!")

def playerLose():
    print("You lose.")


def blackjackGame():
    #Create and shuffle the deck
    newDeck = Deck()
    newDeck.shuffle()

    #Create the player and the dealer hand (empty)
    player1 = Player()
    dealer = Player()

    #Deal 2 cards to each player
    dealer.add_card(newDeck.deal())
    dealer.add_card(newDeck.deal())
    
    player1.add_card(newDeck.deal())
    player1.add_card(newDeck.deal())

    #Show the player the cards before the game starts
    showSome(player1, dealer)
    
    #Start the game
    while playing:
        
        #Ask user whether they want to hit or stand
        hit_or_stand(newDeck, player1)
        
        
        #Show the player their cards and the single dealer card
        showAll(player1, dealer)


        #If user busts code
        if(player1.value > 21):
            player_busts(player1)
            break

        #If user did not bust, continue to dealer:
        if(player1.value <= 21):

            #If dealers cards are less than 17 AND less than the users cards, dealer must hit
            while(dealer.value < 17):
                player_hit(newDeck, dealer)
                if(dealer.value>21):
                    dealer_busts(dealer)
            showAll(player1, dealer)
                #Check if dealer busts


        if(player1.value < 22 and player1.value > dealer.value):
            playerWin()
        
        elif(player1.value < 22 and player1.value < dealer.value):
            playerLose()


    
    




if __name__ == "__main__":
    blackjackGame()

