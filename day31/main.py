from tkinter import *
import pandas as pd
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
LANG_FONT = ("Ariel", 30, "italic")
WORD_FONT = ("Ariel", 60, "bold")
word = None
index = None
data_dict = {}

window = Tk()
window.title("Flashy")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    data_dict = data.to_dict(orient="records")


learned_words = []

def pick_word():
    global word
    global index
    global timer

    window.after_cancel(timer)
    if len(data_dict) > 0:
        word = random.choice(data_dict)
        show_french(word)
        timer = window.after(3000, show_english, word) # window.after can be called anywhere and won't terminate until the time is completed regardless of what else is being computed.
    else:
        canvas.itemconfig(lang_label, text=f"Congratulations", fill="black")
        canvas.itemconfig(word_label, text=f"All Done", fill="black")

def show_french(word):
    canvas.itemconfig(canvas_image, image=flashcard_front_image)
    canvas.itemconfig(lang_label, text=f"French", fill="black")
    canvas.itemconfig(word_label, text=f"{word['French']}", fill="black")

def show_english(word):
    canvas.itemconfig(canvas_image, image=flashcard_back_image)
    canvas.itemconfig(lang_label, text=f"English", fill="white")
    canvas.itemconfig(word_label, text=f"{word['English']}", fill="white")

def correct():
    global word
    learned_words.append(data_dict.pop(data_dict.index(word)))
    pick_word()


timer = window.after(3000, show_english)

flashcard_front_image = PhotoImage(file="images/card_front.png")
flashcard_back_image = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526, highlightthickness=0, background=BACKGROUND_COLOR)
canvas_image = canvas.create_image(400, 263, image=flashcard_front_image)
canvas.grid(column=0, row=0, columnspan=2)

lang_label = canvas.create_text(400, 150, text="", font=LANG_FONT)
word_label = canvas.create_text(400, 263, text="", font=WORD_FONT)

correct_image = PhotoImage(file="images/right.png")
correct_button = Button(text="Correct", image=correct_image, highlightthickness=0, bg="black", command=correct) 
correct_button.grid(column=1, row=1)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(text="Wrong", image=wrong_image, highlightthickness=0, bg="black", command=pick_word)
wrong_button.grid(column=0, row=1)


pick_word()


window.mainloop()
pd.DataFrame(data_dict).to_csv("data/words_to_learn.csv", index=False)
