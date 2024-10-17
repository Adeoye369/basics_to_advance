from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time, random

crome_option = webdriver.ChromeOptions()
crome_option.add_experimental_option("detach", True)

driver = webdriver.Chrome()


# Load main page
driver.get("https://secure-retreat-92358.herokuapp.com/")

time.sleep(3)

fname = driver.find_element(By.NAME, value="fName")
lname = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
submit_btn = driver.find_element("css selector", value=".form-signin .btn")

fname.send_keys("Adeoye")
lname.send_keys("Adegbite")
email.send_keys("teobe@mailman.com")
submit_btn.send_keys(Keys.ENTER)

time.sleep(5)

driver.quit()

