import random
import numpy as np

#This is Second Version [for github reasons]

#Testing update

#Testing yet again

#Last test

#Creating Individual Card Class
class Card:
    def __init__(self, value, suit, fullDeck):
        self.value = value
        self.suit = suit
        self.fullDeck = fullDeck

        value = np.array(["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"])
        suit = np.array(["clubs", "hearts", "diamonds", "spades"])

        fullDeck = np.array(np.meshgrid(value, suit)).T.reshape(52,-1)

    def shuffle(self):
        np.random.shuffle(self.fullDeck)

    def deal(self):
        card = self.fullDeck.pop()
        return card


    
    