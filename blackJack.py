"""
The following two classes include several functions which suopport the smooth game running.
The "Prep" class is used to support the "Game" class, which is the core part of this project. 
The startGame function under main class is how the whole game process goes.

"""

from random import shuffle

class Prep:
    
    def calculator(cards):   
        """ 
        Define a function to calculate the points of cards.
        
        Key Arguments:
        ace_count: count the number of 'A' in hand
        point: Calculate total points of cards in hand
        
        Return Type: int
        
        """

        point = 0
        ace_count = 0 
        
        # calculate points for non-ace cards and count the number of ace
        for i in cards:
            if i in ['J','Q','K']:
                point += 10
            elif i == 'A':
                ace_count += 1            
            else:
                point += int(i)            
        
        # when you have at least 1 ace and one of them can be treated as 11
        if ace_count != 0 and (ace_count - 1) + point <= 10:
            point += (ace_count - 1) + 11
        
        # when you don't have ace or the ace you have can only be treated as 1
        else:
            point += ace_count
        
        return point
        
class Game:
    
    def startGame():
        """
        Define a function to perform the game logic.
    
        Key Arguments:
        
        win: Total winning rounds so far
        round: The number of round as of now
        action_taken: The action taken (hit or stand) according to user's input
        shuffle(deck): Shuffle the deck of cards every six rounds
        player_hand: The cards in player's hand as of now
        dealer_hand: The cards in dealer's hand as of now
        player_point: Total points of player as of now
        dealer_point: Totol points of dealer as of now
    
        """
        round = 1
        win = 0
        while True:

            # create a user input to start every round of the game
            play = input("Press any key to start game, 'N' to exit.").upper()
            
            # if user inputs 'N' or 'n', then the game is over
            if play == 'N':
                break
            
            # shuffle the deck every 6 rounds
            if  round%6 == 1:
                print('------------------------ Round',round,'------------------------')
                deck = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']*4
                shuffle(deck)
                print('                     < Shuffle Deck >                     ')
                
                # use pop() to deal the cards
                player_hand = [deck.pop(),deck.pop()]
                dealer_hand = [deck.pop(),deck.pop()]
                
                # use calculator() in Prep class to calculate points
                dealer_point = Prep.calculator(dealer_hand)
                player_point = Prep.calculator(player_hand)                 
                
                # Show player's cards and points; show dealer's first card 
                print("You have cards:", player_hand,", your points:",player_point)
                print("Dealer has one card facing up:",dealer_hand[0])
                
                while True:
                    # when at least one of player and dealer has 21 at the beginning of this round
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
              
                    else:
                        # if none of the above situations happen, ask the user to hit or stand
                        action_taken = input("    >>> What do you want to do? Press any key to hit, 'S' to stand.        /").upper()
                        
                        # if player choose to hit, pop another card and calculate the new points 
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
                            # if player has less than 21, then ask her again if she wants to hit or stand, until she busted or has blackjack or choose to stand
                
                        else:
                            # if player choose to stand, it's now dealer's turn to look at his cards
                            # use a while loop to deal the cards until dealer hits soft 17 
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
                # print out accumulated win percentage of the player
                print('\n')
                # print out a blank line for readability of the output
                round += 1
                # current round ends, count a new round
            
            
            #For other regular rounds which don't need shuffling deck
            else:
                print('------------------------ Round',round,'------------------------')
                
                # the following codes are the same with line 83 to line 180, because for regular rounds the game logic is the same
                
                player_hand = [deck.pop(),deck.pop()]
                dealer_hand = [deck.pop(),deck.pop()]
                dealer_point = Prep.calculator(dealer_hand)
                player_point = Prep.calculator(player_hand)
                
                print("You have cards:", player_hand,", your points:",player_point)
                print("Dealer has one card facing up:",dealer_hand[0])
                
                while True:

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
                    
                    else:
                        action_taken = input("    >>> What do you want to do? Press any key to hit, 'S' to stand.        /").upper()

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
                
        # if user inputs 'N' or 'n', then print out "Game Over" and exit the game    
        print('Game Over')
        
        return