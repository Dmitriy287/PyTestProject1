from config.config_params1 import *
from test_bankxyz.locator import *
from test_bankxyz.data import *
import allure

@pytest.fixture
def login_bank_customer(browser, selenium_action): # pytest -k login test_step.py
    def login_bank_customer_function():
        browser.get(driver_get_bankxyz)
        selenium_action.action_click_element(locator_button_login_customer)
        allure.step("Делаем скришот:")
        allure.attach(browser.get_screenshot_as_png(), name="screenshot_login_bank_customer", attachment_type=allure.attachment_type.PNG)
    yield login_bank_customer_function

@pytest.fixture
def login_bank_potter(browser, selenium_action): # pytest -k login test_step.py
    def login_bank_potter_function():
        selenium_action.action_click_element(locator_button_your_name)
        selenium_action.action_click_element(locator_button_harry_potter)
        selenium_action.action_click_element(locator_button_your_name_login)
        allure.step("Делаем скришот:")
        allure.attach(browser.get_screenshot_as_png(), name="screenshot_login_bank_potter", attachment_type=allure.attachment_type.PNG)
    yield login_bank_potter_function

@pytest.fixture
def login_bank_customer_hermoine(browser, selenium_action): # pytest -k login test_step.py
    def login_bank_customer_hermoine_function():
        selenium_action.action_click_element(locator_select_hermoine)
        selenium_action.action_wait_on_page(1000)
        selenium_action.action_click_element(locator_select_login_button)
        allure.step("Делаем скришот:")
        allure.attach(browser.get_screenshot_as_png(), name="screenshot_login", attachment_type=allure.attachment_type.PNG)
    yield login_bank_customer_hermoine_function

@pytest.fixture
def login_bank_weasly(browser, selenium_action):  # pytest -k login test_step.py
    def login_bank_weasly_function():
            selenium_action.action_click_element(locator_button_your_name)
            selenium_action.action_click_element(locator_button_ron_weasly)
            selenium_action.action_click_element(locator_button_your_name_login)
            allure.step("Делаем скришот:")
            allure.attach(browser.get_screenshot_as_png(), name="screenshot_login_bank_weasly", attachment_type=allure.attachment_type.PNG)
    yield login_bank_weasly_function

@pytest.fixture
def bank_home(browser, selenium_action):
    def bank_home_function():
            selenium_action.action_click_element(locator_button_bank_home)
            allure.step("Делаем скришот:")
            allure.attach(browser.get_screenshot_as_png(), name="screenshot_bank_home", attachment_type=allure.attachment_type.PNG)
    yield bank_home_function

@pytest.fixture
def logout_bank(browser, selenium_action):
    def logout_bank_function():
            selenium_action.action_click_element(locator_button_logout)
            allure.step("Делаем скришот:")
            allure.attach(browser.get_screenshot_as_png(), name="screenshot_logout_bank", attachment_type=allure.attachment_type.PNG)
    yield logout_bank_function

@pytest.fixture
def deposit(browser, selenium_action):
    def deposit_function():
            selenium_action.action_click_element(locator_button_count_select)
            selenium_action.action_click_element(locator_count_1005)
            selenium_action.action_click_element(locator_button_deposit)
            selenium_action.action_click_element(locator_field_amount)
            selenium_action.action_fill_input(locator_field_amount, data_deposit)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_click_element(locator_confirm_deposit)
            allure.step("Делаем скришот:")
            allure.attach(browser.get_screenshot_as_png(), name="screenshot_deposit_function", attachment_type=allure.attachment_type.PNG)
    yield deposit_function

@pytest.fixture
def withdrawl(browser, selenium_action):
    def withdrawl_function():
            selenium_action.action_click_element(locator_button_count_select)
            selenium_action.action_click_element(locator_count_1005)
            selenium_action.action_click_element(locator_button_withdrawl)
            selenium_action.action_click_element(locator_field_amount)
            selenium_action.action_fill_input(locator_field_amount, data_withdrawl)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_click_element(locator_confirm_withdrawl)
            allure.step("Делаем скришот:")
            allure.attach(browser.get_screenshot_as_png(), name="screenshot_withdrawl", attachment_type=allure.attachment_type.PNG)
    yield withdrawl_function

@pytest.fixture
def transaction(browser, selenium_action):
    def transaction_function():
            selenium_action.action_click_element(locator_button_transactions)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_click_element(locator_scroll_right)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_click_element(locator_transactions_reset)
            allure.step("Делаем скришот:")
            allure.attach(browser.get_screenshot_as_png(), name="screenshot_transaction", attachment_type=allure.attachment_type.PNG)
    yield transaction_function

@pytest.fixture
def login_bank_manager(browser, selenium_action):
    def login_bank_manager_function():
        browser.get(driver_get_bankxyz)
        selenium_action.action_click_element(locator_button_login_bank_manager)
        allure.step("Делаем скришот:")
        allure.attach(browser.get_screenshot_as_png(), name="screenshot_login_bank_manager", attachment_type=allure.attachment_type.PNG)
    yield login_bank_manager_function

@pytest.fixture
def add_customer(browser, selenium_action):
    def add_customer_function():
            selenium_action.action_click_element(locator_button_add_customer)
            selenium_action.action_fill_input(locator_first_name, data_first_name)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_fill_input(locator_last_name, data_last_name)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_fill_input(locator_post_code, data_post_code)
            selenium_action.action_wait_on_page(1000)
            selenium_action.action_click_element(locator_button_add_customer_confirm)
            selenium_action.action_accept_alert()
            allure.step("Делаем скришот:")
            allure.attach(browser.get_screenshot_as_png(), name="screenshot_add_customer", attachment_type=allure.attachment_type.PNG)
    yield add_customer_function

@pytest.fixture
def open_account(browser, selenium_action):  # pytest -k login test_step.py
    def open_account_function():
        selenium_action.action_click_element(locator_button_open_account)
        selenium_action.action_click_element(locator_customer_name)
        selenium_action.action_click_element(locator_customer_potter)
        selenium_action.action_click_element(locator_currency)
        selenium_action.action_click_element(locator_currency_rupee)
        selenium_action.action_click_element(locator_button_process)
        allure.step("Делаем скришот:")
        allure.attach(browser.get_screenshot_as_png(), name="screenshot_open_account", attachment_type=allure.attachment_type.PNG)
    yield open_account_function

@pytest.fixture
def list_customer(browser, selenium_action):
    def list_customer_function():
        selenium_action.action_click_element(locator_button_list_customer)
        selenium_action.action_wait_on_page(1000)
        allure.step("Делаем скришот:")
        allure.attach(browser.get_screenshot_as_png(), name="screenshot_login", attachment_type=allure.attachment_type.PNG)
    yield list_customer_function
