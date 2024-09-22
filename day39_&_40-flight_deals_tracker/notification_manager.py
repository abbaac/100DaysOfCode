import smtplib
import os

class NotificationManager:
    def __init__(self):
        self.user = "warw1zrd@gmail.com"
        self.password = os.getenv('WARW1ZRD_API_KEY')
        
        if self.password:
            print("Password loaded successfully")
        else:
            print("Failed to load password")

    def send_mail(self, mailing_list, message_body):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=self.user,
                            password=self.password)
            for email in mailing_list:
                connection.sendmail(from_addr=self.user, to_addrs=email, msg=message_body) 

