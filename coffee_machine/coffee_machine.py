from tkinter import Menu
from tokenize import ContStr
from resources import MENU
from resources import resources

# #Define coin types
quarters = 0
dimes = 0
nickels = 0
pennies = 0

#Set initial resources
water = resources['water']
milk = resources['milk']
coffee = resources['coffee']
money = 0.00
cost = 0.00

#check resources
def check_resources(drink_choice, water, milk, coffee):
    drink = MENU[drink_choice]
    ingred = drink['ingredients']
    drink_water = ingred["water"]
    drink_coffee = ingred['coffee']
    if 'milk' in ingred:
        drink_milk = ingred['milk']

    if drink_water > water:
        print('Sorry there is not enough water.')
    elif drink_milk is not None and drink_milk > milk:
        print('Sorry there is not enough milk.')
    elif drink_coffee > coffee:
        print('Sorry there is not enough coffee.')

def drink_cost(drink_cost):
    drink = MENU[drink_cost]
    cost = drink['cost']
    return cost

#deduct the ingredients of the drink from the resources
def make_coffee(drink_choice, water, milk, coffee):
    drink = MENU[drink_choice]
    ingred = drink['ingredients']
    drink_water = ingred['water']
    drink_coffee = ingred['coffee']
    if 'milk' in ingred:
        drink_milk = ingred['milk']
    
    water = water - drink_water
    coffee = coffee - drink_coffee
    milk = milk - drink_milk
    print(f'Here is your {drink_choice} ☕️. Enjoy!')
    

def process_coins(quarters, dimes, nickels, pennies):
# this can be done with an input, like total = input(how many quarters) * 0.25, then repeat for each type of coin
    quarter_money = quarters * 0.25
    dimes_money = dimes * 0.10
    nickels_money = nickels *  0.05
    pennies_money = pennies * 0.01
    total_money = quarter_money + dimes_money + nickels_money + pennies_money
    return money + total_money
    

#make 3 hot flavors, espresso, latte, cappuccino, secret prompts of 'report' and 'off'

machine_on = True

while machine_on:

    prompt = input(f"What would you like? (espresso/latte/cappuccino): ")

    if prompt == 'report':
        print(f'Water: {water}ml')
        print(f'Milk: {milk}ml')
        print(f'Coffee: {coffee}g')
        print(f'Money: ${money}')

    elif prompt == 'off':
        machine_on = False
    
    else:
        drink_choice = prompt

    check_resources(drink_choice, water, milk, coffee)

    print('Please insert coins.')

    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickels = int(input('How many nickels?: '))
    pennies = int(input('How many pennies?: '))

    money = process_coins(quarters, dimes, nickels, pennies)
    print(money)
    # If too much money is provided, return the change.
    if money > cost:
        change = float(money - cost)
        print(f'Here is ${round(change,2)} in change.')
        money = money - cost

    make_coffee(drink_choice, water, milk, coffee)

# TODO correct prices not being captured and added to the cost
# TODO deducting amounts of items from resources is not accurate

'''def make_coffee():
for item in order_ingredients:
    resources[item] = order_ingredients[item]
    print('Here is your drink')'''