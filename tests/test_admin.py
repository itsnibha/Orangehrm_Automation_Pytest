from utils.config import DASHBOARD_URL,USERNAME,PASSWORD,BASE_URL,ROLE,EMPLOYEE
def test_admin_Valid_username(admin_page,driver):
    admin_page.enter_username("USERNAME")
    admin_page.click_search_button()
    assert "viewSystemUsers" in driver.current_url
def test_user_role(admin_page,driver):
    admin_page.select_user_role("Admin")
    admin_page.click_search_button()
    assert "viewSystemUsers" in driver.current_url
def test_employee_name(admin_page,driver):
    admin_page.enter_employee_name("EMPLOYEE")
    admin_page.click_search_button()
    assert "viewSystemUsers" in driver.current_url
def test_status(admin_page,driver):
    admin_page.select_status("status")
    admin_page.click_search_button()
    assert "viewSystemUsers" in driver.current_url
def test_search(admin_page,driver):
    admin_page.enter_username(USERNAME)
    admin_page.select_status("USER_ROLE")
    admin_page.enter_employee_name(EMPLOYEE)
    admin_page.click_search_button()
    assert "viewSystemUsers" in driver.current_url
def test_reset_username(admin_page,driver):
    admin_page.enter_username(USERNAME)
    admin_page.click_reset_button()
    assert admin_page.get_username_value() == ""
def test_reset_user_role(admin_page,driver):
    admin_page.select_user_role(ROLE)
    admin_page.click_reset_button()
    assert admin_page.get_role_value().strip() == "-- Select --"
def test_reset_employee_name(admin_page,driver):
    admin_page.enter_employee_name(EMPLOYEE)
    admin_page.click_reset_button()
    assert admin_page.get_employee_name_value() == ""
def test_reset_status(admin_page,driver):
    admin_page.select_status("STATUS")
    admin_page.click_reset_button()
    assert admin_page.get_status_value().strip() == "-- Select --"
def test_reset(admin_page,driver):
    admin_page.enter_username(USERNAME)
    admin_page.select_status("USER_ROLE")
    admin_page.enter_employee_name(EMPLOYEE)
    admin_page.select_status("STATUS")
    admin_page.click_reset_button()
    assert admin_page.get_username_value() == ""
    assert admin_page.get_role_value().strip() == "-- Select --"
    assert admin_page.get_employee_name_value() == ""
    assert admin_page.get_status_value().strip() == "-- Select --"
def test_add_user(admin_page,driver):
    admin_page.click_add_user_button()
    admin_page.select_status("USER_ROLE")
    admin_page.enter_employee_name(EMPLOYEE)
    admin_page.select_status("STATUS")
    admin_page.enter_username(USERNAME)
    admin_page.enter_password(PASSWORD)
    admin_page.enter_confirm_password(PASSWORD)
    admin_page.click_save_button()
def test_delete(admin_page,driver):
    admin_page.select_check_box()
    admin_page.click_delete_button()
    admin_page.get_sure_message()
    admin_page.click_sure_delete_button()


