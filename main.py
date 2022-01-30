## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import art
import random

def blackjack_math(sum_cards):
    running_total = 0
    for card in range(0,len(sum_cards)):
        running_total += sum_cards[card]
    return running_total

        

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_again = True
while play_again == True:
    print(art.logo)
    player = [cards[random.choice(cards)], cards[random.choice(cards)]]
    print(f"player cards are: {player}, your score is {blackjack_math(player)}")

    dealer = [cards[random.choice(cards)], cards[random.choice(cards)]]
    print(f"dealer cards are: [{dealer[0]}, X] ")

    while blackjack_math(dealer) < 17:
        dealer.append(random.choice(cards))

    hitting = True
    while hitting:
        hit_stay = input("Would like to hit or stay? h or s: ")
        if hit_stay == "h":
            player.append(random.choice(cards))
            print(f"player cards are: {player}, your score is {blackjack_math(player)}")
            if blackjack_math(player) > 21:
                for i in player:
                    if i == 11:
                        i = 1
                break
            

                    
        if hit_stay == "s":
            break
        else:
            continue
        
    print("\n \n \n \n")
    print(player)
    print(dealer)

    losing_prompt = (f"your score was {blackjack_math(player)}\ndealer score was {blackjack_math(dealer)}\n you LOSE") 
    tie_prompt = (f"your score was {blackjack_math(player)}\ndealer score was {blackjack_math(dealer)}\n tie game")
    winning_prompt = (f"your score was {blackjack_math(player)}\ndealer score was {blackjack_math(dealer)}\n you WIN")
    

    # losing scenarios
    if blackjack_math(player) > 21:
        print(losing_prompt)
    elif blackjack_math(player) < blackjack_math(dealer) and blackjack_math(dealer) <= 21:
        print(losing_prompt)

    # tie scenarios
    elif blackjack_math(player) == blackjack_math(dealer):
        print(tie_prompt)

    # winning prompts
    elif blackjack_math(dealer) > 21:
        print(winning_prompt)
    elif blackjack_math(dealer) < blackjack_math(player):
        print(winning_prompt)
    elif blackjack_math(player) == 21:
        print(winning_prompt)
    else:
        "ERROR"
    again = input("Would you like to play again? y or n: ")
    if again == "y":
        continue
    else:
        break




