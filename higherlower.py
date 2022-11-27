from art import logo
from game_data import data
import random
from replit import clear
# display art

def format_data(account):
    account_name = account["name"]
    account_descr = account["description"]
    account_country = account["country"]
    return f"{account_name}, a {account_descr}, from {account_country}"

def check_answer(guess, a_follower_count, b_followers_count):
    '''Take the user guess and follower counts and returns if they get it right.'''
    if a_follower_count > b_follower_count:
        return guess == 'a'
    else:
        return guess == 'b'

print(logo)
score = 0
game_should_continue = True
account_b = random.choice(data)
#make the game repeatable

while game_should_continue:
    # Generate a random account from the game data.

    # Make account at position B become the next account at position A.
    account_a = account_b
    account_b = random.choice(data)

    if account_a == account_b:
        account_b = random.choice(data)

    #Format the account data into printable format.

    print(f"Compare A: {format_data(account_a)} ")
    print(vs)
    print(f"Against B: {format_data(account_b)} ")

    # Ask user for a guess.
    guess = input("Who has more followers? A or B?: ").lower()

    # Check if user is correct.
    # Get follower count of each acount
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]

    is_correct = check_answer(guess, a_follower_count, b_follower_count)

# Clear the screen between rounds.
    clear()
    print(logo)
    ## use if statement to check if user is correct.
    if is_correct:
        score +=1
        print(f"You're right! Current score: {score}.")
    else:
        game_should_continue = False
        print(f"You're wrong! Current score: {score}.")



# Score keeping

# Make the game repeatable.



