import smtplib
import datetime as dt
import random

# now = dt.datetime.now()
# year = now.year
# day_of_week = now.weekday()  #Monday as 0, Tuesday as 1 and so on
# date_of_birth = dt.datetime(year=2003, month=8, day=13, hour=4)

# if year == 2020:
#     print("Wear a face mask")
# else:
#     print("You're good.")

# print(day_of_week)
# print(date_of_birth)

# print(type(year))



MY_EMAIL = "warw1zrd@gmail.com"
MY_PASSWORD = "rdznsmwavrrwtzfu"


now = dt.datetime.now()
day_of_the_week = now.weekday()

print(day_of_the_week)
if day_of_the_week == 0:
    with open("quotes.txt", "r") as txt:
        quote = random.choice(txt.readlines())

    with smtplib.SMTP("smtp.gmail.com") as connection:     #When we write using the "with command as varibale" format, we dont need to close it at the end e.g connection.close()
        connection.starttls() #TLS stands for Transport Layer Security which encrypts our sent messages for protection incase of interception
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL,  
                            to_addrs="warw1zrd@yahoo.com", 
                            msg=f"Subject: Monday Motivation\n\n{quote}")
