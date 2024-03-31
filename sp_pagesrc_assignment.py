# Pagesource

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Initialise web driver and launch the url
driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# login to website using valid credentials
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# Fetch the Page title
page_Title = driver.title
time.sleep(3)
print("Title:", page_Title)

# Fetch the current url
current_url = driver.current_url
time.sleep(3)
print("current_url:", current_url)

# Extract the entire contents of page into text file
source = driver.page_source
time.sleep(3)
with open("Webpage_task_11.txt", "w", encoding="utf-8") as file:
   file.write(source)
time.sleep(3)
driver.quit()

