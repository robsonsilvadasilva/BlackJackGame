# Black Jack Game - Under Construction
# Version 15/sep/19

import random

suits = ('Hearts','Diamonds','Spades','Clubs')
        
rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 
        'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,'Seven':7, 'Eight':8,'Nine':9,
            'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}


class Card:

    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    
    def __init__(self):
        self.deck = []
        for i in suits:
            for j in rank:
                self.deck.append(Card(i,j))

    def __str__(self):
        deck_comp = ''
        for card in self.deck:
            deck_comp += '\n' + card.__str__()
        
        return 'The deck has: '+ deck_comp
    
    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop()

teste_deck = Deck()
teste_deck.shuffle()
print(teste_deck)

