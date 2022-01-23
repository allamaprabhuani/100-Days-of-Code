import random
from logo import art
from time import sleep

playagain = 'y'

def AceCardValue(DealtCard, player):
    if DealtCard == 1 and sum(player)<21:
        return 11
    else: return DealtCard

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

while playagain.casefold() == 'y':
    print(art)
    dealer = random.choices(cards,k=2)
    player = random.choices(cards,k=2)
    print("Dealer's Cards: ", dealer[0], '#')
    print("Your Cards: ", player[0], player[1])

    dealerwins = "Dealer Wins. Better luck next time."
    playerwins = "You win!"
    actionmsg = '\n Press "D" to Draw another card, or "H" to hold:  '

    action = input(actionmsg)

    #if action.upper() == "D":

    while action.upper() == "D":

        DealtCard = random.choice(cards)
        DealtCard = AceCardValue(DealtCard,player)  #assigning A = 11 if sum(player)<21
        player.append(DealtCard)
        print(f"Your cards:  {' '.join(map(str,player))} || Totals {sum(player)}")

        if sum(player) > 21:
            print(dealerwins)
            break
        elif sum(player) == 21:
            print('Black Jack!', playerwins)
            break
        action = input(actionmsg)
        if action.upper() == 'H':
            continue
        elif action.upper() != 'D':  #other than D or H
            print('Invalid Input. Try again')
            break

    else: #action.upper() == "H":
        print(f"Dealer's Cards:  {' '.join(map(str,dealer))} || Totals {sum(dealer)}")
        if sum(dealer)>16 and sum(player)>sum(dealer):
            print(playerwins)
        
        while sum(dealer)<17:
            print('Dealer Draws...')
            sleep(2)
            DealtCard = random.choice(cards)
            DealtCard = AceCardValue(DealtCard,dealer) #assigning A = 11 if sum(dealer)<21
            dealer.append(DealtCard)
            print(f"Dealer's Cards:  {' '.join(map(str,dealer))} || Totals {sum(dealer)}")
            sleep(2)
        if sum(dealer) > 21 or sum(dealer) < sum(player):
            print(playerwins)
        elif sum(dealer) == sum(player):
            print("Its a Tie.")
        elif sum(dealer) == 21:
            print("BlackJack!", dealerwins)
        else:
            print(dealerwins)
        playagain = input("Do you want to play again? Type 'Y' or 'N' ")