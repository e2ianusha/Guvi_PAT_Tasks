from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By

# Initialize Chrome WebDriver
driver = webdriver.Chrome() 

# Open the Droppable page
url = 'https://jqueryui.com/droppable'
driver.get(url)
time.sleep(2)  # Wait for page to load

# Find the iframe element
iframe_element = driver.find_element(By.TAG_NAME,'iframe')

# Switch to the iframe
driver.switch_to.frame(iframe_element)

# Locate the draggable white box
draggable_element = driver.find_element(By.ID,'draggable')

# Locate the droppable yellow box
droppable_element = driver.find_element(By.ID,'droppable')

# Perform the drag-and-drop operation
actions = ActionChains(driver)
actions.drag_and_drop(draggable_element, droppable_element).perform()

# Wait for a moment to see the result
time.sleep(2)

# Close the browser
driver.quit()
