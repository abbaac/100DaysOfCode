from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep Chrome driver open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# driver = webdriver.Chrome(options=chrome_options)

# driver.get("https://a.co/d/fI2f9za")

# dollar_price = driver.find_element(By.CLASS_NAME, "a-price-whole")  # Getting element by Class Name
# dollar_cents = driver.find_element(By.CLASS_NAME, "a-price-fraction")
#
# product_name = driver.find_element(By.CSS_SELECTOR, "#title span")  # Getting element through CSS format
#
# search_bar = driver.find_element(By.ID, "nav-search")  # Getting element by ID
#
# monthly_buy = driver.find_element(By.XPATH,
#                                   value='//*[@id="social-proofing-faceout-title-tk_bought"]/span')  # Getting element via XPath, use single quotes due to Regex
#
# print(f"The price is {dollar_price.text}.{dollar_cents.text}.")
# print(f"The product name is {product_name.text}.")
# print(f"The size of the search bar is {search_bar.size}.")
# print(f"Monthly buy is '{monthly_buy.text}'.")

# driver.close()  # Close active tab
# driver.quit()  # Close entire browser

driver_2 = webdriver.Chrome(options=chrome_options)
driver_2.get("https://www.python.org/")

event_time = driver_2.find_element(By.CLASS_NAME, value="event-widget").find_element(By.CLASS_NAME, "menu").find_elements(By.TAG_NAME, "time")
event_name = driver_2.find_element(By.CLASS_NAME, value="event-widget").find_element(By.CLASS_NAME, "menu").find_elements(By.TAG_NAME, "a")

event_time = [time.text for time in event_time]
event_name = [name.text for name in event_name]

# print(event_time, event_name)
event_data = {idx: {"time": event_time[idx], "name": event_name[idx]} for idx in range(len(event_time))}

print(event_data)

driver_2.quit()  # Close entire browser

