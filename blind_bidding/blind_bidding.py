from os import system
from art import logo


print(logo)
print("\nWelcome to the secret auction program.")

bid_data = {}

def init_auction():
    name = input("What is your name?: ")
    bid = input("What's your bid?: ₹")
    bid_data[name] = bid
    more_bidders = input('Are there any other bidders? Type \'yes\' or \'no\'.')
    
    if more_bidders[0].casefold() == 'y':
        system('cls')
        init_auction()
    else:
        winner = max(bid_data, key = bid_data.get)
        winning_bid = bid_data.get(winner, 'error')
        print(f'The winner is {winner} with a bid of ₹{winning_bid}')

init_auction()
