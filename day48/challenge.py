from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(chrome_options)
driver.get("http://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.NAME, value="fName")
first_name.send_keys("Abba")

last_name = driver.find_element(By.NAME, value="lName")
last_name.send_keys("Ali-Concern")

email = driver.find_element(By.NAME, value="email")
email.send_keys("aaliconcern@gmail.com")

sign_up_button = driver.find_element(By.TAG_NAME, value="button")
sign_up_button.click()
