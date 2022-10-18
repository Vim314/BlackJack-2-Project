import random
import numpy as np

#This is Second Version [for github reasons]

#Testing update

#Testing yet again

#Last test

#Creating Individual Card Class
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit
    
    value = np.array(["ace", 2, 3, 4, 5, 6, 7, 8, 9, 10, "jack", "queen", "king"])
    suit = np.array(["clubs", "hearts", "diamonds", "spades"])

    print(value[3])