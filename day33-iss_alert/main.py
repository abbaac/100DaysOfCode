import requests
import datetime as dt
import smtplib
import time


MY_LAT = 6.455057
MY_LONG = 3.394179

USERNAME = "warw1zrd@gmail.com"
PASSWORD = "rdznsmwavrrwtzfu"  

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()

    data = response.json()

    latitude = float(data["iss_position"]["latitude"])
    longitude = float(data["iss_position"]["longitude"])
    
    if ((MY_LAT - 5) <= latitude <= (MY_LAT + 5)) and ((MY_LONG - 5) <= longitude <= (MY_LONG + 5)):
        return True
    else:
        return False


def is_dark():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "tzid": "Africa/Lagos",
        "formatted": 0,
    }

    current_hour = dt.datetime.now().hour

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()

    data = response.json()
    sunrise = data["results"]["sunrise"] 
    sunset = data["results"]["sunset"]
    sunsrise_hour = int(sunrise.split("T")[1].split(":")[0]) 
    sunset_hour =int(sunset.split("T")[1].split(":")[0])
    
    if current_hour >= sunset_hour or  current_hour <= sunsrise_hour:
        return True

while True:
    if is_dark() and is_iss_overhead():    
        time.sleep(60)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=USERNAME,
                            password=PASSWORD)
            connection.sendmail(from_addr=USERNAME, to_addrs=USERNAME, msg="Subject:ISS Crossing\nGo outside and look up. You may see the ISS passing!")

