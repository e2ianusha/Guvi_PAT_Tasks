from selenium import webdriver
from selenium.webdriver.common.by import By

# Initialize the Chrome WebDriver
driver=webdriver.Chrome()

# Open the Instagram profile page
username = 'guviofficial'
url = f'https://www.instagram.com/{username}/'
driver.get(url)

# Find the followers count element using Relative XPATH
followers_element = driver.find_element(By.XPATH, '//*[@id="mount_0_0_lz"]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/ul/li[2]/button/span')
followers_count = followers_element.text

# Find the following count element using Relative XPATH
following_element = driver.find_element(By.XPATH, '//*[@id="mount_0_0_lz"]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/ul/li[3]/button/span') 
following_count = following_element.text

# Print the results
print(f"Followers: {followers_count}")
print(f"Following: {following_count}")

# Close the WebDriver
driver.quit()
