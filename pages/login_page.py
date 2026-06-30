from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class LoginPage:
    username_field = (By.NAME, "username")
    password_field = (By.NAME, "password")
    login_button = (By.CSS_SELECTOR, "button[type='submit']")
    error_message = (By.CSS_SELECTOR, ".oxd-alert-content.oxd-alert-content--error")
    required_message=(By.CSS_SELECTOR,".oxd-text.oxd-text--span.oxd-input-field-error-message.oxd-input-group__message")

    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
        self.driver.get(url)
        self.wait.until(EC.visibility_of_element_located(self.username_field))

    def enter_username(self, username):
        field = self.wait.until(EC.element_to_be_clickable(self.username_field))
        field.clear()
        field.send_keys(username)

    def enter_password(self, password):
        field = self.wait.until(EC.element_to_be_clickable(self.password_field))
        field.clear()
        field.send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.login_button).click()
    def click_login(self):
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()


    def is_on_login_page(self):
        return "/auth/login" in self.driver.current_url

    def get_error_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.error_message)
        ).text
    def get_required_message(self):
        return self.wait.until(EC.visibility_of_element_located(self.required_message)).text