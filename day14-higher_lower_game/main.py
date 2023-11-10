import art
from game_data import data
from replit import clear
from random import choice

def challenge():
    return choice(data)

def report(account):
    return f'{account["name"]}, a {account["description"]}, from {account["country"]}.' 

def compare(first, second):
    """Function to check which of the options has a higher or lower amount of followers."""
    if first["follower_count"] > second["follower_count"]:
        return "a"
    else:
        return "b"

def game():
    print(art.logo)
    score = 0
    option_1 = challenge()
    option_2 = challenge()
    resume = True

    while resume:
        while option_2 == option_1:
            option_2 = challenge()
        print(f"Compare A: {report(option_1)}")
        print(art.vs)
        print(f"Against B: {report(option_2)}")
        choice = input("Who has more followers? Type 'A' or 'B': ").lower()
        clear()
        print(art.logo)
        if choice == compare(option_1, option_2):
            score+=1    
            print(f"You're right. Current score: {score}")
            option_1 = option_2
        else:
            print(f"Sorry that's wrong. Final score: {score}")
            resume = False

game()

