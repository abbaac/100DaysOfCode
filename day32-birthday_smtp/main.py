##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.

import pandas as pd
import datetime as dt
import os
import random
import smtplib
from dotenv import load_dotenv

load_dotenv()


now = dt.datetime.now()
MY_USER = "warw1zrd@gmail.com"
MY_PASSWORD = os.getenv('WARW1ZRD_API_KEY')
# print(now.year, now.month, now.day)


birthday_df = pd.read_csv("birthdays.csv").to_dict(orient="records")
for birthday in birthday_df:
    if (now.month, now.day) == (birthday["month"], birthday["day"]):
        
        messages = os.listdir("letter_templates")
        message = random.choice(messages)
        
        with open(f"letter_templates/{message}", "r") as file:
            new_message = file.read()
            new_message = new_message.replace("[NAME]", birthday["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_USER, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_USER, 
                                to_addrs=birthday["email"], 
                                msg=f"Subject: Happy Birthday {birthday['name']}\n\n{new_message}")



