rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

weapons = [rock, paper, scissors]
options = []

user_choice = int(input("Welcome to the Rock, Paper, Scissors game.\nType 0 for Rock, 1 for Paper and 2 for Scissors: "))



if 0 <= user_choice <= 2:
  options.append(user_choice)
  print(f"\n{weapons[user_choice]}")

  computer_choice = random.randint(0, 2)
  options.append(computer_choice)
  print(f"Computer chose:\n{weapons[computer_choice]}")

  if options[0] == options[1]:
    print("Draw")
  elif options[0] == 0 and options[1] == 2:
    print("You win!")
  elif options[0] == 2 and options[1] == 0:
    print("Computer Wins")
  elif options[0] == 1 and options[1] == 0:
    print("You Win")
  elif options[0] == 0 and options[1] == 1:
    print("Computer Wins")
  elif options[0] == 2 and options[1] == 1:
    print("You Win")
  elif options[0] == 1 and options[1] == 2:
    print("Computer Wins")
  else:
    print("Invalid Option, you lose.")
else:
  print("Invalid Option, you lose.")
  



