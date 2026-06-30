import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.config import BASE_URL, USERNAME, PASSWORD
from pages.login_page import LoginPage
from pages.admin import AdminPage
@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--disable-blink-features=AutomationControlled")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()
@pytest.fixture
def login_page(driver):
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    return login_page
@pytest.fixture
def admin_page(driver):
    login_page = LoginPage(driver)
    login_page.open(BASE_URL)
    login_page.login(USERNAME, PASSWORD)
    page = AdminPage(driver)
    page.click_admin_menu()
    page.click_user_management()
    page.click_users()
    return page
