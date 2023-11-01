import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from faker import Faker


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--window-size=100,400')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()


@pytest.fixture
def wait(driver):
    wait = WebDriverWait(driver, timeout=10)
    return wait


@pytest.fixture
def fake_email():
    faker = Faker()
    return faker.email()
