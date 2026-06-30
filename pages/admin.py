from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class AdminPage:
    admin_menu = (By.XPATH, "//span[text()='Admin']")
    user_management=(By.XPATH, "//span[normalize-space()='User Management']")
    users=(By.XPATH, "//a[normalize-space()='Users']")
    username=(By.XPATH, "//label[text()='Username']/ancestor::div[contains(@class,'oxd-input-group')]//input")
    user_role=(By.XPATH,"//label[text()='User Role']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")
    employee_name=(By.XPATH,"//input[@placeholder='Type for hints...']")
    status=(By.XPATH,"//label[text()='Status']/ancestor::div[contains(@class,'oxd-input-group')]//div[contains(@class,'oxd-select-text')]")
    search_button=(By.CSS_SELECTOR,"button[type='submit']")
    reset_button=(By.XPATH,"//button[normalize-space()='Reset']")
    add_user_button = (By.XPATH, "//button[normalize-space()='Add']")
    password=(By.XPATH, "(//input[@type='password'])[1]")
    confirm_password=(By.XPATH, "(//input[@type='password'])[2]")
    save_button=(By.XPATH,"//button[normalize-space()='Save']")
    delete_button = (By.XPATH, "//button[contains(@class,'oxd-button--label-danger')]")

    check_box=(By.XPATH,"(//span[contains(@class,'oxd-checkbox-input')])[1]")
    sure_message=(By.CSS_SELECTOR,"div[role='document']")
    sure_delete_button=(By.XPATH,"//button[normalize-space()='Yes, Delete']")
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
            self.driver.get(url)
    def click_admin_menu(self):
        self.wait.until(
            EC.element_to_be_clickable(self.admin_menu)
        ).click()
        print(self.driver.current_url)

    def click_user_management(self):
        self.wait.until(
            EC.element_to_be_clickable(self.user_management)
        ).click()

    def click_users(self):
        self.wait.until(
            EC.element_to_be_clickable(self.users)
        ).click()
    def enter_username(self, username):
        field = self.wait.until(EC.element_to_be_clickable(self.username))
        field.clear()
        field.send_keys(username)
    def select_user_role(self, role):
        self.wait.until(
            EC.element_to_be_clickable(self.user_role))
    def enter_employee_name(self,employee_name):
        field = self.wait.until(EC.element_to_be_clickable(self.employee_name))
        field.clear()
        field.send_keys(employee_name)
    def select_status(self, role):
        self.wait.until(
            EC.element_to_be_clickable(self.status))
    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()
    def click_reset_button(self):
        self.driver.find_element(*self.reset_button).click()
    def click_add_user_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.add_user_button)
        ).click()
    def get_username_value(self):
        field = self.wait.until(
            EC.visibility_of_element_located(self.username)
        )
        return field.get_attribute("value")

    def get_role_value(self):
        return self.driver.find_element(*self.user_role).text
    def get_employee_name_value(self):
        field = self.wait.until(
            EC.visibility_of_element_located(self.employee_name)
        )
        return field.get_attribute("value")
    def get_status_value(self):
        return self.driver.find_element(*self.status).text

    def enter_password(self, password):
        field = self.wait.until(
            EC.element_to_be_clickable(self.password)
        )
        field.clear()
        field.send_keys(password)

    def enter_confirm_password(self, password):
        field = self.wait.until(
            EC.element_to_be_clickable(self.confirm_password)
        )
        field.clear()
        field.send_keys(password)




    def click_save_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.save_button)
        ).click()
    def click_delete_button(self):
        self.wait.until(
            EC.element_to_be_clickable(self.delete_button)
        ).click()

    def get_sure_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.sure_message)
        ).text
    def click_sure_delete_button(self):
        self.driver.find_element(*self.sure_delete_button).click()

    def select_check_box(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.check_box)
        )
        checkbox.click()





