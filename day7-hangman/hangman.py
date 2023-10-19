import random
from hangman_art import stages, logo
from hangman_words import word_list
from replit import clear

game_over = False

word = random.choice(word_list)
#word = word_list[random.randint(0,2)]
blanks = ["_" for i in range(len(word))]
guess_bank = []

print(logo)
lives = 6
while not game_over:
    print(" ".join(blanks))
    guess = input("\nChoose a letter you feel may be in the hidden word: ").lower()
    clear()
    if guess not in guess_bank:
        guess_bank.append(guess)
        if guess not in word_list:
            if guess in word:
                for idx, i in enumerate(word):
                    if guess == i:
                        blanks[idx] = guess
                print("Yay, you got a word!")
            else:
                lives -=1
                print("That's not part of the words, you lose a life :(")
                print(stages[lives])


            

            if not "_" in blanks:
                game_over = True
                print("\n Congratulations, You Win !")
            elif lives == 0:
                game_over = True
                print("\nYou've been hanged!")
                print("================")
                print(stages[0])
                print(f"\nThe word was {word}!")
    else:
        print(f"You've already chosen {guess}. Choose a different option.")