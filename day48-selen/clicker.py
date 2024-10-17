from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

# enter the website 
driver.get("https://orteil.dashnet.org/experiments/cookie/")
time.sleep(3)


cookie_clicks = 0 
cursor_count = 0
grandma_count = 0


def get_price(id):
    cookie_val_html = driver.find_element(By.ID, value=id)
    value_element = str(cookie_val_html.get_attribute('innerHTML'))

    # isolate the price
    init_pos = value_element.rfind("i>")+2
    end_pos = value_element.find("</b>")
    return int(value_element[init_pos:end_pos].strip().replace(",", ""))


timeout = time.time() + 5
exit_time = time.time() + (60*3) # 3 minute run

# get cookie
cookie = driver.find_element(By.ID, value="cookie")

# click 5 times
while time.time() < exit_time:
    cookie.click()
    time.sleep(0.01)

    if time.time() > timeout:
        # Get initial money
        cookie_clicks = int(driver.find_element(By.ID, value="money").text)
        print(cookie_clicks)
        
        if cookie_clicks > get_price(id="buyGrandma") and grandma_count <= 4:
            driver.find_element(By.ID, "buyGrandma").click()
            grandma_count+=1

        timeout = time.time() + 5

    

    
# close the browser
driver.quit()
