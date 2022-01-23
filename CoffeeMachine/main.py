MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk": 0,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def report():
    available_resources()
    if resources.get('money'):
        money = resources['money']
        print(f'Money: ${money}')


def available_resources():
    print('Available Resources:')
    water = resources['water']
    milk = resources['milk']
    coffee = resources['coffee']
    print(f'\tWater: {water}ml')
    print(f'\tMilk: {milk}ml')
    print(f'\tCoffee: {coffee}g')


def required_resources(item):
    print('Required Resources:')
    water = MENU[item]['ingredients']['water']
    milk = MENU[item]['ingredients']['milk']
    coffee = MENU[item]['ingredients']['coffee']
    print(f'\tWater: {water}ml')
    print(f'\tMilk: {milk}ml')
    print(f'\tCoffee: {coffee}g')


def enough_resources(item):
    for ingredient in MENU[item]['ingredients']:
        if resources[ingredient] <= MENU[item]['ingredients'][ingredient]:
            print(f'Sorry there is not enough {ingredient}.')
            return False
    return True


def process_coins():
    print('Insert Coins: ')
    quarters = 0.25 * int(input('How many quarters?: '))
    nickels = 0.05 * int(input('How many nickels?: '))
    dimes = 0.1 * int(input('How many dimes?: '))
    pennies = 0.01 * int(input('How many pennies?: '))
    return quarters + nickels + dimes + pennies


def transaction_successful(item):
    if enough_resources(item):
        money = process_coins()
        if money >= MENU[item]['cost']:
            if resources.get('money'):
                resources['money'] += MENU[item]['cost']
            else:
                resources['money'] = MENU[item]['cost']
            change = money - MENU[item]['cost']
            if change > 0:
                print(f'Here is ${round(change, 2)} in change.')
            return True
        else:
            print("Sorry that's not enough money. Money refunded.")
            return False



def make_coffee(item):
    if transaction_successful(item):
        resources['water'] = resources['water'] - MENU[item]['ingredients']['water']
        resources['milk'] = resources['milk'] - MENU[item]['ingredients']['milk']
        resources['coffee'] = resources['coffee'] - MENU[item]['ingredients']['coffee']
        print(f"Here's your {item} ☕. Enjoy!")


userInput = 'on'

while userInput != 'off':
    userInput = input('What would you like? (espresso/latte/cappuccino): ')

    if userInput == 'report':
        report()
    elif userInput in MENU.keys():
        make_coffee(userInput)
        