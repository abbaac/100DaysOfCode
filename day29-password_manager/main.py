from tkinter import *
from tkinter import messagebox
import random


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    random_letters = [random.choice(letters) for _ in range(nr_letters)]
    random_symbols = [random.choice(symbols) for _ in range(nr_symbols)]
    random_numbers = [random.choice(numbers) for _ in range(nr_numbers)]

    password_list = random_letters + random_symbols + random_numbers

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_input.get()
    email_name = email_input.get()
    password_name = password_input.get()

    if len(website_name) == 0 or len(password_name) == 0 or len(email_name) == 0:
        messagebox.showerror(title="Error", message="Please fill in all the fields.")
    else:
        verify = messagebox.askyesno(title=website_name, message=f"These are the details entered:\nUsername:{email_name}\nPassword:{password_name}\nIs it okay to save?")
        if verify:
            with open("data.txt", "a") as txt:
                txt.write(f"{website_name} | {email_name} | {password_name}\n")

            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Manager")
# window.minsize(240, 240)
window.config(padx=50, pady=50)


padlock_image = PhotoImage(file="logo.png") 
canvas = Canvas(width=200, height=200)
canvas.create_image(100, 100, image=padlock_image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_input = Entry(width=52)
website_input.grid(column=1, row=1, columnspan=2)
website_input.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_input = Entry(width=52)
email_input.grid(column=1, row=2, columnspan=2)
email_input.insert(0, "aaliconcern@gmail.com")

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_input = Entry(width=33)
password_input.grid(column=1, row=3)


generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()