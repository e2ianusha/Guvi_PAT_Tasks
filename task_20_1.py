'''
Open the URL and Click on “Create FAQ” and “Partners” Links
'''


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Open the URL
driver.get("https://www.cowin.gov.in/")

# Wait for the page to load
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.TAG_NAME, "body")))

# Find the "Create FAQ" anchor tag and click it
faq_link = driver.find_element(By.LINK_TEXT, "FAQ")
faq_link.click()

# Find the "Partners" anchor tag and click it
partners_link = driver.find_element(By.LINK_TEXT, "PARTNERS")
partners_link.click()

'''
Fetch the Opened Windows/Frame IDs and Display Them
'''

# Get the window handles (IDs) of the newly opened windows
window_handles = driver.window_handles

# Print the window handles
for i, handle in enumerate(window_handles):
    print(f"Window {i+1} ID: {handle}")


'''
Close the New Windows and Return to the Home Page
'''

# Close the newly opened windows
for handle in window_handles[1:]:
    driver.switch_to.window(handle)
    driver.close()

# Switch back to the original window
driver.switch_to.window(window_handles[0])

# Print a success message
print("Successfully opened and closed new windows.")

# Close the browser
driver.quit()



