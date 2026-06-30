# OrangeHRM Automation Testing Framework

## Overview

This project is a Selenium-Python automation framework developed using **PyTest** for testing the **OrangeHRM** web application.

The framework follows the **Page Object Model (POM)** design pattern to improve code readability, maintainability, and reusability.

Currently, automation has been implemented for the following modules:

- Login Module
- Admin Module

---

## Tech Stack

- Python
- Selenium WebDriver
- PyTest
- Page Object Model (POM)
- HTML Test Reports
- Chrome WebDriver

---

## Project Structure

```
Orange_Hrm/
│
├── pages/
│   ├── login_page.py
│   └── admin.py
│
├── tests/
│   ├── test_login.py
│   └── test_admin.py
│
├── utils/
│   └── config.py
│
├── reports/
│   └── report.html
│
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## Folder Description

### pages/

Contains all Page Object classes.

- `login_page.py` → Login page locators and methods
- `admin.py` → Admin module locators and methods

---

### tests/

Contains all test scripts.

- `test_login.py`
    - Valid Login
    - Invalid Login
    - Login validations

- `test_admin.py`
    - Navigate to Admin Module
    - Add User
    - Search User
    - Delete User 

---

### utils/

Contains utility files.

- `config.py`
    - Base URL
    - Username
    - Password
    - Other reusable configurations

---

### reports/

Stores generated HTML reports after test execution.

Example:

```
report.html
```

---

### conftest.py

Contains common fixtures such as:

- WebDriver initialization
- Browser setup
- Browser teardown

---

### pytest.ini

Contains PyTest configuration.

Example:

- Test discovery
- HTML report configuration
- Command-line options

---

## Features

- Page Object Model (POM)
- Reusable WebDriver fixtures
- HTML Test Report
- Easy Maintenance
- Modular Framework
- Configurable Test Data

---

## Test Scenarios

### Login Module

✔ Valid Login

✔ Invalid Login

✔ Verify Dashboard after Login

---

### Admin Module

✔ Open Admin Page

✔ Search Existing User

✔ Add New User

✔ Verify Added User

✔ Delete User 

---

## Installation

### Clone Repository

```bash
git clone https://github.com/your-username/OrangeHRM-Automation-pytest.git
```

Move into the project directory:

```bash
cd OrangeHRM-Automation-pytest
```

---

## Create Virtual Environment

Windows

```bash
python -m venv .venv
```

Activate

```bash
.venv\Scripts\activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run Test Cases

Run all tests

```bash
pytest
```

Run with verbose mode

```bash
pytest -v
```

Run a specific test file

```bash
pytest tests/test_login.py -v
```

Run Admin tests

```bash
pytest tests/test_admin.py -v
```

---

## Generate HTML Report

```bash
pytest --html=reports/report.html --self-contained-html
```

After execution, open:

```
reports/report.html
```

to view the detailed test report.

---

## Framework Workflow

```
Test Case
      │
      ▼
PyTest
      │
      ▼
Page Object Model
      │
      ▼
Selenium WebDriver
      │
      ▼
OrangeHRM Application
      │
      ▼
HTML Report
```

---

## Prerequisites

- Python 3.14.5
- Google Chrome
- ChromeDriver (compatible with installed Chrome version)
- pip

---

## Best Practices Followed

- Page Object Model (POM)
- Reusable Fixtures
- Centralized Configuration
- Clean Folder Structure
- Explicit Waits
- Reusable Methods
- HTML Reporting
- Easy Scalability

---

## Future Enhancements

- Data-Driven Testing
- Cross Browser Testing
- Jenkins CI/CD Integration
- GitHub Actions
- Screenshot on Failure
- Logging using Python Logging
- Excel/CSV Test Data
- All OrangeHRM Modules Automation

---

## Author

**Nibha Sah**

QA Automation Engineer

---

## License

This project is created for learning and automation practice purposes.
