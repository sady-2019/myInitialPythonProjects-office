#blackjack or 21 game
#import random
import random

#dealer card
dealer_card =[]

#player card
player_card =[]

#play dealer and display
while len(dealer_card)!=2:
    dealer_card.append(random.randint(1,11))
    if len(dealer_card)==2:
        print("Dealer has X and  ",dealer_card[1])


# play player and display
while len(player_card)!=2:
    player_card.append(random.randint(1,11))
    if len(player_card)==2:
        print("You have ",player_card)


#compare dealer and player
while sum(player_card)<21:
    action=str(input("Do you want to hit or stay: "))
    if action== "hit":
        player_card.append(random.randint(1,11))
        print("You now have total : " + str(sum(dealer_card)) + "from your card", player_card)
    else:
        print("Dealer has total : " + str(sum(dealer_card)) + "from his card", dealer_card)
        print("You have total : " + str(sum(dealer_card)) + "from your card", player_card)
        if sum(player_card)<sum(dealer_card):
            print("You win!!")
        elif sum(player_card)>sum(dealer_card):
            print ("Dealer wins!")
            break

#if player sum is less than dealer then dealer wins
#if player sum is more than dealer then player wins
#if player sum is more than 21 player busted!!
if sum(player_card)>21:
    print("You Busted and Dealer wins")
#if dealer sum is more than 21 dealer busted!!
elif sum(dealer_card)>21:
    print("You win because Dealer Busted")