from idlelib.run import Executive
from time import sleep

from pages.pim import pimpage
from utils.config import VALID_EMPLOYEE_NAME, INVALID_EMPLOYEE_NAME, VALID_EMPLOYEE_ID, INVALID_EMPLOYEE_ID, \
    SUPERVISOR_NAME, EMPLOYEE_FIRST_NAME, EMPLOYEE_MIDDLE_NAME, EMPLOYEE_LAST_NAME,EMPLOYEE_ID


def test_pim_search_Valid_employee_name(pim_page,driver):
    pim_page.enter_employee_name("VALID_EMPLOYEE_NAME")
    pim_page.click_search_button()
    assert "viewEmployeeList" in driver.current_url
def test_pim_search_invalid_employee_name(pim_page,driver):
    pim_page.enter_employee_name(INVALID_EMPLOYEE_NAME)
    pim_page.click_search_button()
    assert pim_page.get_no_records_message() == "No Records Found"
def test_pim_search_valid_employee_id(pim_page,driver):
    pim_page.enter_employee_id(VALID_EMPLOYEE_ID)
    pim_page.click_search_button()
    assert "viewEmployeeList" in driver.current_url
def test_pim_search_invalid_employee_id(pim_page,driver):
    pim_page.enter_employee_id(INVALID_EMPLOYEE_ID)
    pim_page.click_search_button()
    assert pim_page.get_no_records_message() == "No Records Found"
def test_pim_search_employee_status(pim_page,driver):
    pim_page.select_employee_status("Freelance")
    pim_page.click_search_button()
    assert pim_page.get_selected_employee_status() == "Freelance"
def test_pim_search_include(pim_page,driver):
    pim_page.select_include("Past Employees Only")
    pim_page.click_search_button()
    assert pim_page.get_selected_include() == "Past Employees Only"
def test_pim_search_supervisor_name(pim_page,driver):
    pim_page.enter_supervisor_name(SUPERVISOR_NAME)
    pim_page.click_search_button()
    assert "viewEmployeeList" in driver.current_url
def test_pim_search_job_title(pim_page,driver):
    pim_page.select_job_title("Chief Executive officer")
    pim_page.click_search_button()
    assert pim_page.get_selected_job_title() == "Chief Executive officer"
def test_pim_search_sub_unit(pim_page,driver):
    pim_page.select_sub_unit("OrangeHRM")
    pim_page.click_search_button()
    assert pim_page.get_selected_sub_unit() == "OrangeHRM"
def test_reset(pim_page,driver):
    pim_page.select_employee_status("Freelance")
    pim_page.click_reset_button()
    assert pim_page.get_selected_employee_status().strip() == "-- Select --"
def test_add(pim_page,driver):
    pim_page.click_add_button()
    pim_page.enter_employee_first_name(EMPLOYEE_FIRST_NAME)
    pim_page.enter_employee_middle_name(EMPLOYEE_MIDDLE_NAME)
    pim_page.enter_employee_last_name(EMPLOYEE_LAST_NAME)
    pim_page.enter_add_employee_id(EMPLOYEE_ID)
    pim_page.click_save_button()
def test_add_blank_employee_details(pim_page,driver):
    pim_page.click_add_button()
    pim_page.enter_add_employee_id(EMPLOYEE_ID)
    pim_page.click_save_button()
    assert pim_page.get_required_message() == "Required"
def test_blank_eid(pim_page,driver):
    pim_page.click_add_button()
    pim_page.enter_employee_first_name(EMPLOYEE_FIRST_NAME)
    pim_page.enter_employee_middle_name(EMPLOYEE_MIDDLE_NAME)
    pim_page.enter_employee_last_name(EMPLOYEE_LAST_NAME)
    pim_page.click_save_button()
    assert pim_page.get_required_message() == "Required"
def test_delete(pim_page,driver):
    pim_page.select_check_box()
    pim_page.click_delete_button()
    pim_page.get_sure_message()
    pim_page.click_sure_delete_button()

