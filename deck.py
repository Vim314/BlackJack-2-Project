from cgi import test
from hashlib import new
import random
import numpy as np
import sys
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
        print(card)
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

    def aceFix(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

newDeck = Deck()
newDeck.shuffle()


player1 = Player()
player1.add_card(newDeck.deal())
player1.add_card(newDeck.deal())
player1.add_card(newDeck.deal())
print(player1)
player1.aceFix()
print(player1)