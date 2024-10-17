from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# enter the website 
driver.get("https://orteil.dashnet.org/experiments/cookie/")
time.sleep(3)

# Get the cookie
cookie = driver.find_element(By.ID, value="cookie")

# Get upgrade items id
items = driver.find_elements(By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]
print(item_ids)

# Get all upgrade prices
all_prices = driver.find_elements(By.CSS_SELECTOR, value="#store b")
prices = [price.text.split('-')[-1].replace(',','') for price in all_prices]
print(prices)


driver.quit()