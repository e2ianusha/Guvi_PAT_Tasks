from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class IMDbSearchPage:
    URL = "https://www.imdb.com/search/name/"
    SEARCH_BOX = (By.ID, "search-main")
    SEARCH_BUTTON = (By.XPATH, "//button[@data-testid='hero-search-submit']")
    PAGE_TITLE = (By.XPATH, "//h1[contains(text(),'Results for')]")

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def fill_search_criteria(self, search_term, profession, category, language):
        search_input = self.driver.find_element(*self.SEARCH_BOX)
        search_input.clear()
        search_input.send_keys(search_term)
        
        # Select profession
        profession_dropdown = self.driver.find_element(By.ID, "name_type")
        profession_dropdown.click()
        profession_option = self.driver.find_element(By.XPATH, f"//select[@id='name_type']/option[text()='{profession}']")
        profession_option.click()
        
        # Select category
        category_dropdown = self.driver.find_element(By.ID, "known_for")
        category_dropdown.click()
        category_option = self.driver.find_element(By.XPATH, "//select[@id='known_for']/option[text()='{category}']")
        category_option.click()
        
        # Select language
        language_dropdown = self.driver.find_element(By.ID, "birth_place")
        language_dropdown.click()
        language_option = self.driver.find_element(By.XPATH, "//select[@id='birth_place']/option[text()='{language}']")
        language_option.click()

    def click_search_button(self):
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()

    def get_page_title(self):
        return self.driver.find_element(*self.PAGE_TITLE).text