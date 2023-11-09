from art import logo
import random
from replit import clear

def number():
    return random.randint(0,100)

resume = True
while resume:
    clear()
    print(logo)
    print("Welcome to the number guessing gamae.\nI'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty == "easy":
        chances = 10
    else:
        chances = 5

    answer = number()
    not_solved = True
    while not_solved:
        print(f"You have {chances} attempts remaining to guess the number.")
        choice = int(input("Make a guess: "))
        if choice > answer:
            print("Too high.")
            chances-=1
        elif choice < answer:
            print("Too low.")
            chances-=1
        else:
            print(f"You got it. The answer was {answer}.")
            not_solved = False
        if chances > 0:
            print("Guess again")
        else:
            print("You've run out of guesses, you lose.")
            not_solved=False

    bool = input("Would you like to play again? y/n: ").lower()
    if bool == "y":
        resume = True
    else:
        resume = False  
