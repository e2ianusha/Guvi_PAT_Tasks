
# cookies before login and after login
#saucedemo.com

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# cookies before login

print("cookies before login")
for cookies in driver.get_cookies():
   print(cookies)
time.sleep(5)

driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

# cookies after login
print(" cookies after login")
for cookies in driver.get_cookies():
   print(cookies)
time.sleep(5)

# logout
driver.find_element(By.ID, "react-burger-menu-btn").click()
time.sleep(3)
driver.find_element(By.ID, "logout_sidebar_link").click()
time.sleep(3)
driver.quit()