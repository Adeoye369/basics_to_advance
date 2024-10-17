from selenium import webdriver
from selenium.webdriver.common.by import By
import time

crome_options = webdriver.ChromeOptions()
crome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=crome_options)
driver.get("https://www.python.org")

time.sleep(5) # wait 5 secs.

# === find by "CSS_SELECTOR"
event_dates = driver.find_elements(By.CSS_SELECTOR, value="div.event-widget ul.menu li > time")
event_names = driver.find_elements(By.CSS_SELECTOR, value="div.event-widget ul.menu li > a")

event_dates = [date.get_attribute("datetime")[:10] for date in event_dates]
event_names = [name.text for name in event_names]

event_data = {}
# for date, name in zip(event_dates, event_names):
#     current_idx = event_names.index(name) # get current index on element
#     new_data = {current_idx : {date : name}} # Create a new dictionary base on index
#     event_data.update(new_data) # extend/update the dict. data


for i in range(len(event_names)):
    event_data[i] = {
            "time": event_dates[i],
            "event" : event_names[i]
            }

print(event_data)


driver.quit()

