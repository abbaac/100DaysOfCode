import requests
from dotenv import load_dotenv
import os
# from sample_data import data
import datetime as dt
import smtplib
import html

load_dotenv()

STOCK = "IBM"
COMPANY_NAME = "IBM"


ALPHA_VANTAGE_API_KEY = os.getenv('ALPHA_VANTAGE')
NEWS_API_KEY = os.getenv('NEWS_API')

MY_USER = "warw1zrd@gmail.com"
MY_PASSWORD = os.getenv('WARW1ZRD_API_KEY')

def get_stock_status():
        
    today = dt.datetime(year=2024, month=9, day=6).date()
    yesterday = today - dt.timedelta(days=1)
    day_before_yesterday = today - dt.timedelta(days=2)

    parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": ALPHA_VANTAGE_API_KEY,
    }

    response = requests.get(url="https://www.alphavantage.co/query", params=parameters)
    response.raise_for_status()

    data = response.json()
    new_data = data["Time Series (Daily)"]
    data_list = [value for (key, value) in new_data.items()]
    yesterday_close = float(data_list[0]["4. close"])
    day_before_yesterday_close = float(data_list[1]["4. close"])

    change = ((yesterday_close - day_before_yesterday_close ) / yesterday_close) * 100
    if change >=0.5:
        return f"{STOCK}: UP {abs(int(change))}%"
    elif change <= -0.5: 
        return f"{STOCK}: DOWN {abs(int(change))}%"


def get_news(change):
    parameters = {
        "qInTitle": COMPANY_NAME,
        "apiKey": NEWS_API_KEY, 
        # os.getenv("NEWS_API"),
    }

    response_2 = requests.get(url="https://newsapi.org/v2/everything", params=parameters)
    response_2.raise_for_status()

    data = response_2.json()["articles"][:3]
    formatted_articles = [f"{change} Headline: {news['title']}. \nBrief: {news['description']}" for news in data]
    for article in formatted_articles:
        # print(article)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_USER, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_USER, 
                                to_addrs=MY_USER,
                                msg=f"Subject:Daily Stock Alert for {COMPANY_NAME}\n{article}")


alert = get_stock_status()
if alert:
    get_news(alert)







## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

