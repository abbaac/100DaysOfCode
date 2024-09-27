import requests
from bs4 import BeautifulSoup
import os
import smtplib
from dotenv import load_dotenv

load_dotenv()


URL = "https://www.amazon.com/dp/B075CYMYK6?psc=1&ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6"
TARGET_PRICE = 100
USERNAME = "warw1zrd@gmail.com"
PASSWORD = os.getenv('WARW1ZRD_API_KEY')


headers = {'Accept-Language': "en-GB,en-US;q=0.9,en;q=0.8",
           'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/128.0.0.0 Safari/537.36"}

response = requests.get(url=URL, headers=headers)
response.raise_for_status()
data = response.text


soup = BeautifulSoup(data, "html.parser")
price = soup.select("span.a-offscreen")
product_name = soup.find(name="span", id="productTitle").getText().strip()
price = float(price[0].getText().split("$")[1].strip())

# print(soup)

if price <= TARGET_PRICE:
    print(price)
    print(product_name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=USERNAME, password=PASSWORD)
        connection.sendmail(from_addr=USERNAME, to_addrs=USERNAME, msg=f"Subject: Price Drop Alert\n{product_name} is"
                                                                       f"now selling for ${price} on Amazon! Click "
                                                                       f"the link below to buy now!\n{URL}".encode("UTF-8"))