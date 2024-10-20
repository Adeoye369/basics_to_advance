from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from prettyprinter import pprint
import requests, time


# Scrapping the zillow-clone website online
response = requests.get("https://appbrewery.github.io/Zillow-Clone/")
html_doc = response.text

soup = BeautifulSoup(html_doc, "html.parser")

house_data = []
houses_html = soup.select(selector=".StyledPropertyCardDataWrapper")
house1 = houses_html[0]

for house in houses_html:
    info = {}
    info["addr"] = house.find('a').get_text().strip().replace("|","," )
    info["price"] = house.find(class_="PropertyCardWrapper__StyledPriceLine").get_text().strip().split('/')[0].replace("+","")
    info["link"] = house.find('a').get('href')
    house_data.append(info)


# Selenium filling the form on google docs

chrom_options = webdriver.ChromeOptions()
chrom_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrom_options)


driver.get("https://docs.google.com/forms/d/e/1FAIpQLSescRSkofMMxnEiZ9VQTHJni15Nn3iOmoqWJkmkSjPDOH4CvQ/viewform?usp=sf_link")
    
# wait 3secs
time.sleep(5)

for info in house_data[:10]:

    # fill the address
    addr_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # addr_form.click()
    addr_form.send_keys(info["addr"], Keys.ENTER)
    time.sleep(1)

    # # fill the price
    price_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # price_form.click()
    price_form.send_keys(info['price'], Keys.ENTER)
    time.sleep(1)


    # # fill in the link
    link_form = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    # link_form.click()
    link_form.send_keys(info['link'], Keys.ENTER)
    time.sleep(1)

    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit.click()

    time.sleep(3)
    
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSescRSkofMMxnEiZ9VQTHJni15Nn3iOmoqWJkmkSjPDOH4CvQ/viewform?usp=sf_link")

    # wait 3secs
    time.sleep(3)




time.sleep(3)
 
driver.quit()