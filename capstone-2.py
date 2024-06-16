import unittest
from selenium import webdriver
import time

class OrangeHRMAdminPageTest(unittest.TestCase):
    def setUp(self):
        # Initialize Chrome WebDriver
        self.driver = webdriver.Chrome()

    def tearDown(self):
        # Close the browser window after each test
        self.driver.quit()

    def test_successful_login(self):
        # Positive test case: Successful login
        self.login("Admin", "admin123")
        # Assert that after successful login, the dashboard is loaded
        self.assertIn("dashboard", self.driver.current_url)

    def test_invalid_username(self):
        # Negative test case: Invalid username
        self.login("invalid_username", "valid_password")
        # Assert that error message is displayed
        error_message = self.driver.find_element_by_id("spanMessage").text
        self.assertIn("Invalid credentials", error_message)

    def test_invalid_password(self):
        # Negative test case: Invalid password
        self.login("valid_username", "invalid_password")
        # Assert that error message is displayed
        error_message = self.driver.find_element_by_id("spanMessage").text
        self.assertIn("Invalid credentials", error_message)

    def test_blank_credentials(self):
        # Negative test case: Blank username and password
        self.login("", "")
        # Assert that error message is displayed
        error_message = self.driver.find_element_by_id("spanMessage").text
        self.assertIn("Username cannot be empty", error_message)

    def test_forgot_password_link(self):
        # Test case to validate the "Forgot Password" link on the login page
        self.driver.get("https://www.orangehrm.com/en/")
        # Find the "Forgot Password" link
        forgot_password_link = self.driver.find_element_by_link_text("Forgot your password?")
        # Click on the "Forgot Password" link
        forgot_password_link.click()
        # Assert that the current URL contains the expected URL for the forgot password page
        self.assertIn("forgotPassword", self.driver.current_url)

    def test_admin_page_header(self):
        # Test case to validate the header on the admin page
        self.login("Admin", "admin123")
        # Navigate to the admin page
        self.driver.find_element_by_id("menu_admin_viewAdminModule").click()
        # Find the header element
        header_element = self.driver.find_element_by_css_selector("div#content h1")
        # Assert that the header text is correct
        self.assertEqual(header_element.text, "Admin")

    def test_admin_page_main_menu(self):
        # Test case to validate the main menu on the admin page
        self.login("Admin", "admin123")
        # Navigate to the admin page
        self.driver.find_element_by_id("menu_admin_viewAdminModule").click()
        # Find the main menu elements
        main_menu_elements = self.driver.find_elements_by_css_selector("div#menu_admin_parentMenu>ul>li>a")
        # Extract main menu text
        main_menu_text = [menu.text for menu in main_menu_elements]
        # Expected main menu items
        expected_main_menu = ["User Management", "Job", "Organization", "Qualifications", "Nationalities", "Configuration"]
        # Assert that the main menu items match the expected main menu items
        self.assertListEqual(main_menu_text, expected_main_menu)

    def login(self, username, password):
        # Open OrangeHRM login page
        self.driver.get("https://opensource-demo.orangehrmlive.com/")
        # Wait for the page to load
        time.sleep(2)
        # Locate the username and password fields and enter credentials
        username_field = self.driver.find_element_by_id("txtUsername")
        password_field = self.driver.find_element_by_id("txtPassword")
        username_field.send_keys(username)
        password_field.send_keys(password)
        # Click on the login button
        login_button = self.driver.find_element_by_id("btnLogin")
        login_button.click()
        # Wait for the page to load
        time.sleep(2)

if __name__ == "__main__":
    unittest.main()