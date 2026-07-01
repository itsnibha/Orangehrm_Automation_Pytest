from xml.etree.ElementInclude import include

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
class pimpage:
    pim_menu=(By.XPATH,"//span[normalize-space()='PIM']")
    employee_name=(By.XPATH,"//label[text()='Employee Name']/../following-sibling::div//input")
    employee_id=(By.XPATH,"//label[text()='Employee Id']/../following-sibling::div//input")

    include=(By.XPATH, "//label[text()='Include']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    employee_status=(By.XPATH, "//label[text()='Employment Status']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    supervisor_name=(By.XPATH,"//label[text()='Supervisor Name']/../following-sibling::div//input")
    job_title=(By.XPATH,"//label[text()='Job Title']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    sub_unit=(By.XPATH, "//label[text()='Sub Unit']/../following-sibling::div//div[contains(@class,'oxd-select-text')]")
    no_records_message=(By.XPATH, "//span[normalize-space()='No Records Found']")
    search_button=(By.XPATH, "//button[@type='submit']")
    reset_button=(By.XPATH,"//button[normalize-space()='Reset']")
    add_button=(By.XPATH,"//button[normalize-space()='Add']")
    employee_first_name=(By.XPATH," //input[@placeholder='First Name']")
    employee_middle_name=(By.XPATH," //input[@placeholder='Middle Name']")
    employee_last_name=(By.XPATH,"//input[@placeholder='Last Name']")
    add_employee_id=(By.XPATH,"//div[@class='oxd-input-group oxd-input-field-bottom-space']//div//input[@class='oxd-input oxd-input--active']")
    save_button=(By.XPATH,"//button[normalize-space()='Save']")
    cancel_button=(By.XPATH,"//button[normalize-space()='Cancel']")
    check_box=(By.XPATH,"(//span[contains(@class,'oxd-checkbox-input')])[1]")
    delete_button = (By.XPATH, "//button[i[contains(@class,'bi-trash')]]")
    sure_message=(By.XPATH,"//div[@role='document']")
    sure_delete=(By.XPATH,"//button[normalize-space()='Yes, Delete']")
    def __init__(self, driver, timeout=15):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def open(self, url):
            self.driver.get(url)
    def click_pim_menu(self):
        self.wait.until(
            EC.element_to_be_clickable(self.pim_menu)
        ).click()
        print(self.driver.current_url)

    def enter_employee_name(self, employee_name):
            field = self.wait.until(EC.element_to_be_clickable(self.employee_name))
            field.clear()
            field.send_keys(employee_name)
    def enter_supervisor_name(self, supervisor_name):
            field = self.wait.until(EC.element_to_be_clickable(self.supervisor_name))
            field.clear()
            field.send_keys(supervisor_name)
    def enter_employee_id(self, employee_id):
            field = self.wait.until(EC.element_to_be_clickable(self.employee_id))
            field.clear()
            field.send_keys(employee_id)
    def click_search_button(self):
        self.driver.find_element(*self.search_button).click()

    def get_no_records_message(self):
        return self.driver.find_element(*self.no_records_message).text

    def select_employee_status(self, employee_status):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.employee_status)
        )
        dropdown.click()
        option = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, f"//div[@role='option']//span[normalize-space()='{employee_status}']")
            )
        )
        option.click()
    def get_selected_employee_status(self):
        return self.driver.find_element(*self.employee_status).text

    def select_include(self, include):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.include)
        )
        dropdown.click()

        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@role='option']")
            )
        )

        for option in options:
            print(option.text)
            if option.text.strip() == include:
                option.click()
                break
    def get_selected_include(self):
        return self.driver.find_element(*self.include).text
    def select_job_title(self,job_title):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.job_title)
        )
        dropdown.click()
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@role='option']")
            )
        )

        for option in options:
            print(option.text)
            if option.text.strip() == job_title:
                option.click()
                break
    def get_selected_job_title(self):
        return self.driver.find_element(*self.job_title).text
    def select_sub_unit(self,sub_unit):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.sub_unit)
        )
        dropdown.click()
        options = WebDriverWait(self.driver, 10).until(
            EC.presence_of_all_elements_located(
                (By.XPATH, "//div[@role='option']")
            )
        )

        for option in options:
            print(option.text)
            if option.text.strip().lower() == sub_unit.lower():
                option.click()
                break
            if option.text.strip() == sub_unit:
                    option.click()
                    print("Clicked:", option.text)
                    break
    def get_selected_sub_unit(self):
        return self.driver.find_element(*self.sub_unit).text
    def click_reset_button(self):
        self.driver.find_element(*self.reset_button).click()
    def click_add_button(self):
        self.driver.find_element(*self.add_button).click()
    def enter_employee_first_name(self, employee_first_name):
            field = self.wait.until(EC.element_to_be_clickable(self.employee_first_name))
            field.clear()
            field.send_keys(employee_first_name)
    def enter_employee_middle_name(self, employee_middle_name):
            field = self.wait.until(EC.element_to_be_clickable(self.employee_middle_name))
            field.clear()
            field.send_keys(employee_middle_name)
    def enter_employee_last_name(self, employee_last_name):
            field = self.wait.until(EC.element_to_be_clickable(self.employee_last_name))
            field.clear()
            field.send_keys(employee_last_name)
    def enter_add_employee_id(self, add_employee_id):
            field = self.wait.until(EC.element_to_be_clickable(self.add_employee_id))
            field.clear()
            field.send_keys(add_employee_id)

    def click_save_button(self):
        self.driver.find_element(*self.save_button).click()

    def get_required_message(self):
        return self.driver.find_element(
            By.XPATH,
            "//span[@class='oxd-text oxd-text--span oxd-input-field-error-message oxd-input-group__message']"
        ).text
    def select_check_box(self):
        checkbox = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.check_box)
        )
        checkbox.click()
    def click_delete_button(self):
        self.driver.find_element(*self.delete_button).click()
    def get_sure_message(self):
        return self.wait.until(
            EC.visibility_of_element_located(self.sure_message)
        ).text
    def click_sure_delete_button(self):
        self.driver.find_element(*self.sure_delete).click()