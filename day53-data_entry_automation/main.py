import time

from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

response = requests.get('https://appbrewery.github.io/Zillow-Clone/')
page = response.text

soup = BeautifulSoup(page, 'html.parser')

houses = soup.find_all("div", class_="StyledPropertyCardPhotoBody")
prices = soup.find_all('span', class_="PropertyCardWrapper__StyledPriceLine")
addresses = soup.find_all('address')

house_links = [house.a['href'] for house in houses]
house_prices = [prices.text.split("+")[0].split("/")[0] for prices in prices]
house_addresses = [address.text.strip().replace("|", "") for address in addresses]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)


for index in range(len(house_links)):
    driver.get("https://forms.gle/WDLMYQHD9NEaJMBA9")
    time.sleep(3)
    address_entry = driver.find_element(By.XPATH,
                                        '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price_entry = driver.find_element(By.XPATH,
                                      '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_entry = driver.find_element(By.XPATH,
                                     '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    address_entry.send_keys(house_addresses[index])
    price_entry.send_keys(house_prices[index])
    link_entry.send_keys(house_links[index])

    button = driver.find_element(By.CLASS_NAME, "NPEfkd")
    button.click()

    redo = driver.find_element(By.CLASS_NAME, "c2gzEf")
    redo.click()

driver.close()