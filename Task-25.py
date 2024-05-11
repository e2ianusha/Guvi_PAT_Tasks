from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Initialize the Chrome driver
driver = webdriver.Chrome()

# Open the IMDb search page
imdb_url = 'https://www.imdb.com/search/name/'
driver.get(imdb_url)

# Wait for the search box to appear and be visible
wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.visibility_of_element_located((By.ID, 'suggestion-search')))
search_box.send_keys('Leonardo DiCaprio')  # Example search query

# Wait for the dropdown menu to appear and be visible
dropdown = wait.until(EC.visibility_of_element_located((By.ID, 'react-autowhatever-navSuggestionSearch')))
dropdown.click()  # Click the dropdown to reveal options
dropdown.find_element(By.XPATH,"//*div[@id='react-autowhatever-navSuggestionSearch--item-1']").click()

# Wait for the search button to be clickable
search_button = wait.until(EC.element_to_be_clickable((By.ID, 'suggestion-search-button')))
search_button.click()

# Close the browser
driver.quit()
