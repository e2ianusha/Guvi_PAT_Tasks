from selenium import webdriver
import os
from selenium.webdriver.common.by import By
import requests
import time


# Set the URL
url = "https://www.labour.gov.in/"

# Initialize the Chrome WebDriver
driver = webdriver.Chrome()

# Navigate to the URL
driver.get(url)

# Find the 'Documents' menu and click on it
documents_menu = driver.find_element(By.LINK_TEXT, "Documents")  # Use By.LINK_TEXT
documents_menu.click()

# Find the link for the monthly progress report and click on it
monthly_progress_report_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Monthly Progress Report')]")
time.sleep(5)
# Execute JavaScript to click on the link
driver.execute_script("arguments[0].click();", monthly_progress_report_link)



# Download the monthly progress report
monthly_progress_report_url = driver.current_url
monthly_progress_report_filename = "monthly_progress_report.pdf"
response = requests.get(monthly_progress_report_url)
with open(monthly_progress_report_filename, "wb") as f:
    f.write(response.content)

# Create a folder for the photo gallery
photo_gallery_folder = "photo_gallery"
os.makedirs(photo_gallery_folder, exist_ok=True)

# Execute JavaScript to navigate to the 'Media' menu
driver.execute_script("window.location.href = '/media';")

driver.find_element(By.LINK_TEXT,"Click for more info of Press Releases").click()


#click on the 'Photo Gallery' sub-menu
driver.find_element(By.LINK_TEXT,"Photo Gallery ")


# Find the first 10 photos and download them
photo_elements = driver.find_elements(By.CSS_SELECTOR, ".gallery-item img")
for i, photo_element in enumerate(photo_elements[:10]):
    photo_url = photo_element.get_attribute("src")
    photo_filename = f"photo_{i+1}.jpg"
    response = requests.get(photo_url)
    with open(os.path.join(photo_gallery_folder, photo_filename), "wb") as f:
        f.write(response.content)

# Print a success message
print(f"Monthly progress report downloaded as {monthly_progress_report_filename}")
print(f"10 photos downloaded and stored in the {photo_gallery_folder} folder")

# Close the WebDriver
driver.quit()