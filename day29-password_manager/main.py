from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json


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

    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website_name = website_input.get()
    user_name = email_input.get()
    password_name = password_input.get()
    dict = {
        website_name:
            {
                "username": user_name,
                "password": password_name
            }
    }

    if len(website_name) == 0 or len(password_name) == 0 or len(user_name) == 0:
        messagebox.showerror(title="Error", message="Please fill in all the fields.")
    else:
        try:
            with open("data.json", "r") as data_file:
                # Load Data
                data = json.load(data_file)
        except FileNotFoundError:
            with open("data.json", "w") as data_file:
                json.dump(dict, data_file, indent=4)
        else:
            # Update Data
            data.update(dict)

            #Save data
            with open("data.json", "w") as data_file:
                json.dump(data, data_file, indent=4)
        finally:
            website_input.delete(0, END)
            password_input.delete(0, END)

# ---------------------------- FIND PASSWORD -------------------------- #
def find_password():
    website_name = website_input.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
            saved_username = data[website_name]["username"]
            saved_password = data[website_name]["password"]
    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data file not found.")
    except KeyError as error:
        messagebox.showerror(title="Error", message=f"No details for {error} exists.")
    else:
        messagebox.showinfo(title=website_name, message=f"Username: {saved_username}\nPassword: {saved_password}")

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

website_input = Entry(width=33)
website_input.grid(column=1, row=1)
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

search_password_button = Button(text="Search", width=14, command=find_password)
search_password_button.grid(column=2, row=1)

generate_password_button = Button(text="Generate Password", width=14, command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)


window.mainloop()