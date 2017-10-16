 #!/usr/bin/python3

"""
@project Name: BlackJack Game Implementation

@author: fl

@date:10/14/2017

The following two classes include several functions which suopport the smooth game running.
Prep class was used to support the main class Game, which is the core part of this small 
project. The startGame function under main class is how the whole game process goes.

"""

#Imports 
from random import shuffle

class Prep:

    def calculator(cards):   
        """ define the function of calculator
        
        Key Arguments:

        ace_count: Handle points when one or more 'A' exist
        point: Calculated total points for on-hand center
        
        Return Type: int
        """
        #initial variables
        point = 0
        ace_count = 0 
        
        #Loop Cards to find counts of 'A'
        for i in cards:
            if i in ['J','Q','K']:
                point += 10
            elif i == 'A':
                ace_count += 1            
            else:
                point += int(i)            
        
        if ace_count != 0 and (ace_count - 1) + point <= 10:
            point += (ace_count - 1) + 11
        
        else:
            point += ace_count
        
        return point
        
class Game:
    
    def startGame():
        """define the function of main class, start the game!
    
        Key Arguments:
        
        win: Total winning rounds so far
        round: The number of round as of now
        action_taken: The desired action from user's input
        shuffle(deck): Reset the order of cards every six rounds
        player_hand: The cards player hold as of now
        dealer_hand: The cards dealer hold as of now
        player_point: Total points of player as of now
        dealer_point: Totol points of dealer as of now
    
        """
        #initial variables
        round = 1
        win = 0
        while True:

            play = input("Press any key to start game, 'N' to exit.").upper()
            
            # if user inputs 'N', then game ends
            if play == 'N':
                break
            
            #shuffle the deck for every 6 rounds
            if  round%6 == 1:
                print('------------------------ Round',round,'------------------------')
                deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4
                shuffle(deck)
                print('                     < Shuffle Deck >                     ')
                player_hand = [deck.pop(),deck.pop()]
                dealer_hand = [deck.pop(),deck.pop()]
                dealer_point = Prep.calculator(dealer_hand)
                player_point = Prep.calculator(player_hand)                 
                
                #Show player and dealer's cards and player points
                print("You have cards:", player_hand,", your points:",player_point)
                print("Dealer has one card facing up:",dealer_hand[0])
                
                while True:
                    #Handle the situation with 21 points from either side
                    if dealer_point == 21 and player_point < 21:
                        print('\n')
                        print('***** Dealer has BLACKJACK and wins *****')
                        print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                        break
                    
                    elif dealer_point == 21 and player_point == 21:
                        print('\n')
                        print('***** You tied the dealer *****')
                        print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                        break
                    
                    elif dealer_point < 21 and player_point == 21:
                        win += 1
                        print('\n')
                        print('***** You have BLACKJACK and win *****')                       
                        print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                        break   
                    
                    #Ask user to choose hitting another card or standing if there is no 21 points
                    else:
                        action_taken = input("    >>> What do you want to do? Press any key to hit, 'S' to stand.        /").upper()
                        #Pree any key to hit another card
                        if action_taken != 'S':
                            player_hand.append(deck.pop())
                            player_point = Prep.calculator(player_hand)
                            print('\n')
                            print("You now have cards:", player_hand,"; Your points:",player_point)
                                
                            if player_point > 21:
                                print('\n')
                                print('***** You busted. Dealer wins *****')
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break
                
                            elif player_point == 21:
                                win += 1
                                print('\n')
                                print('***** You have BLACKJACK and win *****')                       
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break
                            
                            else:
                                continue
                    
                
                        else:
                            while Prep.calculator(dealer_hand) <= 16:
                                dealer_hand.append(deck.pop())
                                dealer_point = Prep.calculator(dealer_hand)
            
                            if dealer_point > 21:
                                win += 1
                                print('\n')
                                print('***** Dealer busted. You win *****')
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break
            
                            elif player_point > dealer_point:
                                win += 1
                                print('\n')
                                print('***** You win *****')
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break 
                            
                            elif player_point < dealer_point:
                                print('\n')
                                print('***** Dealer wins *****')
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break
                            
                            else:
                                print('\n')
                                print('***** You tied the dealer *****')
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break

                
                print('<<< Wins:',win,'. Win Percentage:{:.2%}'.format(win/round),'>>>')
                print('\n')
                round += 1
            
            #For the regular rounds which don't need shuffle
            else:
                print('------------------------ Round',round,'------------------------')
                player_hand = [deck.pop(),deck.pop()]
                dealer_hand = [deck.pop(),deck.pop()]
                dealer_point = Prep.calculator(dealer_hand)
                player_point = Prep.calculator(player_hand)
                
                print("You have cards:", player_hand,", your points:",player_point)
                print("Dealer has one card facing up:",dealer_hand[0])
                
                while True:
                    #Handle the situation with 21 points from either side
                    if dealer_point == 21 and player_point < 21:
                        print('\n')
                        print('***** Dealer has BLACKJACK and wins *****')
                        print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                        break
                    
                    elif dealer_point == 21 and player_point == 21:
                        print('\n')
                        print('***** You tied the dealer *****')
                        print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                        break
                    
                    elif dealer_point < 21 and player_point == 21:
                        win += 1
                        print('\n')
                        print('***** You have BLACKJACK and win *****')                       
                        print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                        break   
                    
                    #Ask user to choose hitting another card or standing if there is no 21 points
                    else:
                        action_taken = input("    >>> What do you want to do? Press any key to hit, 'S' to stand.        /").upper()
                        #Pree any key to hit another card
                        if action_taken != 'S':
                            player_hand.append(deck.pop())
                            player_point = Prep.calculator(player_hand)
                            print('\n')
                            print("You now have cards:", player_hand,"; Your points:",player_point)
                                
                            if player_point > 21:
                                print('\n')
                                print('***** You busted. Dealer wins *****')
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break
                
                            elif player_point == 21:
                                win += 1
                                print('\n')
                                print('***** You have BLACKJACK and win *****')                       
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break
                            
                            else:
                                continue
                    
                
                        else:
                            while Prep.calculator(dealer_hand) <= 16:
                                dealer_hand.append(deck.pop())
                                dealer_point = Prep.calculator(dealer_hand)
            
                            if dealer_point > 21:
                                win += 1
                                print('\n')
                                print('***** Dealer busted. You win *****')
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break
            
                            elif player_point > dealer_point:
                                win += 1
                                print('\n')
                                print('***** You win *****')
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break 
                            
                            elif player_point < dealer_point:
                                print('\n')
                                print('***** Dealer wins *****')
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break
                            
                            else:
                                print('\n')
                                print('***** You tied the dealer *****')
                                print('( Dealer has cards:',dealer_hand,'; Dealer points:',dealer_point,')')
                                break

                #Output winning percentage and total rounds played
                print('<<< Wins:',win,'. Win Percentage:{:.2%}'.format(win/round),'>>>')
                print('\n')
                round += 1
            
        print('Game Over')
        
        return