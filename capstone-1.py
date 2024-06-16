import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class OrangeHRMLoginTest(unittest.TestCase):
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

    def test_add_new_employee(self):
        # Positive test case: Add a new employee in PIM module
        self.login("valid_username", "valid_password")
        # Navigate to the PIM module
        self.driver.find_element_by_id("menu_pim_viewPimModule").click()
        # Click on the Add button to add a new employee
        self.driver.find_element_by_id("btnAdd").click()
        # Enter employee details (you may adjust the fields based on your OrangeHRM setup)
        self.driver.find_element_by_id("firstName").send_keys("John")
        self.driver.find_element_by_id("lastName").send_keys("Doe")
        self.driver.find_element_by_id("btnSave").click()
        # Wait for the page to load
        time.sleep(2)
        # Assert that the new employee is added successfully
        success_message = self.driver.find_element_by_class_name("message").text
        self.assertIn("Successfully Saved", success_message)

    def test_edit_employee_details(self):
        # Positive test case: Edit an existing employee in PIM module
        self.login("valid_username", "valid_password")
        # Navigate to the PIM module
        self.driver.find_element_by_id("menu_pim_viewPimModule").click()
        # Search for the existing employee to edit (you may adjust based on your OrangeHRM setup)
        self.driver.find_element_by_id("empsearch_employee_name_empName").send_keys("John Doe")
        self.driver.find_element_by_id("searchBtn").click()
        # Click on the employee record to edit
        self.driver.find_element_by_link_text("John Doe").click()
        # Modify employee details (for example, change last name)
        self.driver.find_element_by_id("personal_txtEmpLastName").clear()
        self.driver.find_element_by_id("personal_txtEmpLastName").send_keys("Smith")
        # Save changes
        self.driver.find_element_by_id("btnSave").click()
        # Wait for the page to load
        time.sleep(2)
        # Assert that the changes are saved successfully
        success_message = self.driver.find_element_by_class_name("message").text
        self.assertIn("Successfully Updated", success_message)

    def test_delete_employee(self):
        # Positive test case: Delete an existing employee in PIM module
        self.login("valid_username", "valid_password")
        # Navigate to the PIM module
        self.driver.find_element_by_id("menu_pim_viewPimModule").click()
        # Search for the existing employee to delete (you may adjust based on your OrangeHRM setup)
        self.driver.find_element_by_id("empsearch_employee_name_empName").send_keys("John Smith")
        self.driver.find_element_by_id("searchBtn").click()
        # Click on the checkbox next to the employee record
        self.driver.find_element_by_name("chkSelectRow[]").click()
        # Click on the "Delete" button
        self.driver.find_element_by_id("btnDelete").click()
        # Confirm deletion in the popup
        self.driver.find_element_by_id("dialogDeleteBtn").click()
        # Wait for the page to load
        time.sleep(2)
        # Assert that the employee is deleted successfully
        success_message = self.driver.find_element_by_class_name("message").text
        self.assertIn("Successfully Deleted", success_message)

    def login(self, username, password):
        # Open OrangeHRM login page
        self.driver.get("https://www.orangehrm.com/en/")
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