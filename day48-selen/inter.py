from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random

crome_option = webdriver.ChromeOptions()
crome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome()


# Load main page
driver.get("https://www.python.org/")

time.sleep(3)

waits_link = driver.find_element(By.NAME, value="q")
waits_link.send_keys("Ipython")
waits_link.send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()

