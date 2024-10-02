import time
from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

money = driver.find_element(By.ID, "money")

click_cookie = driver.find_element(By.ID, "cookie")
store = driver.find_element(By.ID, "store")

five_min = time.time() + 60*5   # Current world time from Jan 1st 1970 till now in seconds + 5 minutes
interval = time.time() + 1

while True:
    click_cookie.click()
    current_time = time.time()
    if current_time >= interval:
        upgrades = store.find_elements(By.TAG_NAME, "b")
        for index in range(len(upgrades[:-1])-1, -1, -1):
            price = int(upgrades[index].text.split(" - ")[1].replace(",", ""))
            if int(money.text.replace(",", "")) >= price:
                upgrades[index].click()
                break
            interval = time.time() + 1
    if time.time() > five_min:
        break

cps = driver.find_element(By.ID, "cps")
print(cps.text)


driver.close()
