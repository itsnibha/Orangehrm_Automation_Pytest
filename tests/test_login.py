from utils.config import BASE_URL, DASHBOARD_URL, USERNAME, PASSWORD, INVALID_USERNAME, INVALID_PASSWORD, \
    UPPERCASE_USERNAME, UPPERCASE_PASSWORD
from pages.login_page import LoginPage
def test_valid_login(login_page,driver):
    login_page.login(USERNAME, PASSWORD)
    assert driver.current_url == DASHBOARD_URL
# INVALID_USERNAME
def test_invalid_username_login(login_page,driver):
    login_page.login(INVALID_USERNAME, PASSWORD)
    assert login_page.get_error_message() == "Invalid credentials"
# INVALID_PASSWORD
def test_invalid_password_login(login_page,driver):
    login_page.login(USERNAME, INVALID_PASSWORD)
    assert login_page.get_error_message() == "Invalid credentials"
def test_empty_username_login(login_page,driver):
    login_page.login("", PASSWORD)
    assert login_page.get_required_message() == "Required"
def test_empty_password_login(login_page,driver):
    login_page.login(USERNAME,"")
    assert login_page.get_required_message() == "Required"
def test_empty_login(login_page,driver):
    login_page.login("", "")
    assert login_page.get_required_message() == "Required"
def test_uppercase_username_login(login_page,driver):
    login_page.login(UPPERCASE_USERNAME, PASSWORD)
    assert login_page.get_error_message()== "Invalid credentials"
def test_uppercase_password_login(login_page,driver):
    login_page.login(USERNAME, UPPERCASE_PASSWORD)
    assert login_page.get_error_message()== "Invalid credentials"
def test_uppercase_login(login_page,driver):
    login_page.login(UPPERCASE_USERNAME, UPPERCASE_PASSWORD)
    assert login_page.get_error_message()== "Invalid credentials"




