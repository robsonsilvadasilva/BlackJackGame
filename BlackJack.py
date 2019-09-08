##Black Jack Game

import random

class BlackJack:
    
    def deck():

        suits = ('Hearts','Diamonds','Spades','Clubs')
        
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 
        'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        
        values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,'Seven':7, 
        'Eight':8,'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

        for i in range(2):
            p_suits  = random.randint(0,3)
            p_values = random.randint(0,12)
            card = [suits[p_suits], ranks[p_values]]
            print(f'Your cards is {card[0]} of {card[1]} and its value is {values[card[1]]}')

while True:
    game = BlackJack
    game.deck()
    print("Deck again? :")
    if str(input()) == 'y':
        continue
    else:
        break
