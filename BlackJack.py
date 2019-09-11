# Black Jack Game - Under Construction
# Version 11/sep/19

from random import randint

class BlackJack:

    def __init__(self, player_name, player_balance):

        self.player_name = player_name
        self.player_balance = player_balance

    def __str__(self):
        
        return (f'{self.player_name} you are with $ {self.player_balance}\n')

    def start_game(self):
        
        print(f'{self.player_name} you have bet $ {self.player_balance} :)')
        print("\n\nNow, LET'S Start the Game :) \nGood Luck!!!\n\n\n\n\n")
        print('\n'*20)    
    def deck(self,n):

        suits = ('Hearts','Diamonds','Spades','Clubs')
        
        ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 
        'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
        
        values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6,'Seven':7, 
        'Eight':8,'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

        card = []
        sum = 0
        for i in range(n):
            p_suits  = randint(0,3)
            p_values = randint(0,12)
            card.append(f'{suits[p_suits]} of {ranks[p_values]}')
            sum += values[ranks[p_values]] 

        return card, sum

    def print_hand(self, hand, sum, player='Dealer'):
        print(f'{player}:\n---------')
        print(f'*Hand: {sum}\n*{hand}\n')


#------Here starts the main-------------
## INTRODUCTION OF THE GAME 
print('\n'*100)
print('Welcome to the Black Jack Game\n\n\n')
player_name = input('Please, type your name: ')
player_balance = int(input('Please place a bet in $: '))
game = BlackJack(player_name,player_balance)
game.start_game()
print(game)

c = True
while c:
    t = input('Please type c to continue ')
    if t == 'c':
        c = False
    else:
        continue
## FINISHEd THE INTRODUCTION
dealer_hand = []
player_hand = []

main1 = True
main2 = True
while main1:
    print('\n'*100)
    dealer_hand, dealer_sum = game.deck(1)
    player_hand, player_sum = game.deck(2)
    game.print_hand('Dealer', dealer_hand, dealer_sum)
    game.print_hand(player_name, player_hand, player_sum)
    print(f'\n\n{player_name} its your turn!')
    while main2:
        s = str(input(f'Type h to hit s to stay with this hand\n'))
        if s.lower() == 'h':
            swap, hitsum = game.deck(1)
            player_hand.append(swap)
            player_sum += hitsum
            print('\n'*100)
            print(f'This is the result of you hit: {swap}')
            game.print_hand(player_name, player_hand, player_sum)
        elif s.lower() == 's':
            main1 = False
            main2 = False

    #while main3:

