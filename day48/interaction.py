from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

web_driver = webdriver.Chrome(chrome_options)
web_driver.get("https://en.wikipedia.org/wiki/Main_Page")

# no_of_articles = web_driver.find_element(By.CSS_SELECTOR, value='#articlecount a')
# print(no_of_articles.text)

# view_history = web_driver.find_element(By.LINK_TEXT, "View history")
# view_history.click()


search_icon = web_driver.find_element(By.XPATH, value='//*[@id="p-search"]/a')
search_icon.click()

search = web_driver.find_element(By.NAME, value='search')
search.send_keys("Python", Keys.ENTER)

web_driver.close()
