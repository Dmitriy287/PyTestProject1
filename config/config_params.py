import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.ie.service import Service as IeService
from selenium.webdriver.ie.options import Options as IeOptions
from config.action import SeleniumAction
import os


# Функция для получения пути к драйверу
def get_driver_path(browser_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    webdriver_dir = os.path.join(current_dir, "webdrivers")
    if browser_name.lower() == 'chrome':
        return os.path.join(webdriver_dir, "chromedriver.exe")
    elif browser_name.lower() == 'chrome_mob':
        return os.path.join(webdriver_dir, "chromedriver.exe")
    elif browser_name.lower() == 'firefox':
        return os.path.join(webdriver_dir, "geckodriver.exe")
    elif browser_name.lower() == 'firefox_mob':
        return os.path.join(webdriver_dir, "geckodriver.exe")
    elif browser_name.lower() == 'firefoxde':
        return os.path.join(webdriver_dir, "geckodriver.exe")
    elif browser_name.lower() == 'opera':
        return os.path.join(webdriver_dir, "operadriver.exe")
    elif browser_name.lower() == 'yandex':
        return os.path.join(webdriver_dir, "yandexdriver.exe")
    elif browser_name.lower() == 'edge':
        return os.path.join(webdriver_dir, "msedgedriver.exe")
    elif browser_name.lower() == 'edge_mob':
        return os.path.join(webdriver_dir, "msedgedriver.exe")
    elif browser_name.lower() == 'edgeie':
        return os.path.join(webdriver_dir, "msedgedriver.exe")
    elif browser_name.lower() == 'ie64':
        return os.path.join(webdriver_dir, "IEDriverServer64.exe")
    elif browser_name.lower() == 'ie32':
        return os.path.join(webdriver_dir, "IEDriverServer32.exe")
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")


# Фикстура для создания браузера
@pytest.fixture(params=['chrome'])
def browser(request):
    browser_name = request.param
    driver_path = get_driver_path(browser_name)
    if browser_name.lower() == 'chrome':
        service = ChromeService(executable_path=driver_path)
        options_c = ChromeOptions()
        options_c.add_argument("-headless")
        options_c.add_argument("user-agent=Firefox")
        driver = webdriver.Chrome(service=service, options=options_c)
    elif browser_name.lower() == 'chrome_mob':
        service = ChromeService(executable_path=driver_path)
        options_cm = ChromeOptions()
        mobile_emulation = {"deviceName": "iPhone 4"}
        options_cm.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(service=service, options=options_cm)
    elif browser_name.lower() == 'firefox_mob':
        service = FirefoxService(executable_path=driver_path)
        options_fm = FirefoxOptions()
        mobile_emulation = {"deviceName": "iPhone 8"}
        options_fm.add_experimental_option("mobileEmulation", mobile_emulation)
        options_fm.add_argument("user-agent=chrome")
        driver = webdriver.Firefox(service=service, options=options_fm)
    elif browser_name.lower() == 'firefox':
        service = FirefoxService(executable_path=driver_path)
        options_f = FirefoxOptions()
        options_f.add_argument("-headless")
        driver = webdriver.Firefox(service=service, options=options_f)
    elif browser_name.lower() == 'opera':
        service = ChromeService(executable_path=driver_path)
        options_o = ChromeOptions()
        options_o.add_experimental_option('w3c', True)
        driver = webdriver.Chrome(service=service, options=options_o)
    elif browser_name.lower() == 'yandex':
        service = ChromeService(executable_path=driver_path)
        options_y = ChromeOptions()
        options_y.add_experimental_option('w3c', True)
        driver = webdriver.Chrome(service=service, options=options_y)
    elif browser_name.lower() == 'edge':
        service = EdgeService(executable_path=driver_path)
        options_e = EdgeOptions()
        options_e.add_argument("user-agent=Firefox")
        driver = webdriver.Chrome(service=service, options=options_e)
    elif browser_name.lower() == 'edge_mob':
        service = EdgeService(executable_path=driver_path)
        options_em = EdgeOptions()
        mobile_emulation = {"deviceName": "iPhone 4"}
        options_em.add_experimental_option("mobileEmulation", mobile_emulation)
        driver = webdriver.Chrome(service=service, options=options_em)
    elif browser_name.lower() == 'edgeie':
        service = EdgeService(executable_path=driver_path)
        options_e_ie = EdgeOptions()
        options_e_ie.add_argument("--force-legacy-default-referrer-policy")
        options_e_ie.add_argument("--use-old-msedge-rendering")
        options_e_ie.add_argument("--use-old-msedge-ua")
        driver = webdriver.Ie(service=service, options=options_e_ie)
    elif browser_name.lower() == 'ie64':
        service = IeService(executable_path=driver_path)
        options_ie = IeOptions()
        driver = webdriver.Ie(service=service, options=options_ie)
    elif browser_name.lower() == 'ie32':
        service = IeService(executable_path=driver_path)
        options_ie = IeOptions()
        driver = webdriver.Ie(service=service, options=options_ie)
    elif browser_name.lower() == 'firefoxde':
        firefoxde_dir = r"C:\Program Files\Firefox Developer Edition\firefox.exe"
        service = FirefoxService(executable_path=driver_path)
        options_fde = FirefoxOptions()
        options_fde.binary_location = firefoxde_dir
        driver = webdriver.Firefox(service=service, options=options_fde)
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    yield driver
    driver.quit()


# Фикстура для создания объекта SeleniumAction
@pytest.fixture
def selenium_action(browser):
    selenium_action = SeleniumAction(browser)
    yield selenium_action