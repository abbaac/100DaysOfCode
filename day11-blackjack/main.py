from art import logo
import random
from replit import clear
from time import sleep
############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def add_card(list):
    """Adds a random card from the deck to the input list"""
    list.append(random.choice(deck))
    return list

def status(player_list, comp_list):
    """Prints the player's sum and the computers first card."""
    print(f"\tYour cards: {player_list}, current score: {sum(player_list)}")
    print(f"\tComputer's first card: {comp_list[0]}")

def compare(player_list, comp_list):
        print(f"Your final hand: {player_list}, final score: {sum(player_list)}")
        print(f"Computer's final hand: {comp_list}, final score: {sum(comp_list)}")
        if sum(player_list) > 21:
            print("You went over, you lose.")
        elif sum(player_list) == 21 and len(player_list) == 2:
            print("You win with a blackjack!")
        elif sum(comp_list) == 21 and len(comp_list) == 2:
            print("Computer won with a blackjack")
        elif 21 >= sum(comp_list) > sum(player_list):
            print("Computer won. You lost.")
        elif 21 < sum(comp_list):
            print("Computer went over, you win!")
        elif sum(comp_list) == sum(player_list):
            print("It's a draw.")
        else:
            print("You win!")



def game():
    player = []
    comp = []
    blackjack = False

    for i in range(2):
        player, comp = add_card(player), add_card(comp)

    if sum(player) == 21 or sum(comp) == 21:
        blackjack = True

    status(player, comp)
    while blackjack != True and sum(player) <= 21:
        choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
        if choice == "y":
            player = add_card(player)
            if sum(player) > 21 and 11 in player:
                player.remove(11)
                player.append(1)
            status(player, comp)
        else:
            while sum(comp) < 17:
                comp = add_card(comp)
            break
    compare(player, comp)
    sleep(2)

resume = True
while resume:
    print(logo)
    play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if play == "y":
        game()
    else:
        resume = False
