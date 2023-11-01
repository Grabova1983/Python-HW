import time

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


@pytest.fixture
def chrome_options():
    options = Options()
    options.add_argument('--window-size=100,400')
    return options


@pytest.fixture
def driver(chrome_options):
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_loading_website(driver):
    driver.get('https://victoretc.github.io/selenium_waits/')
    # if driver.find_element((By.CSS_SELECTOR, 'body > h1')).text == "Практика с ожиданиями в Selenium":

    test_button = driver.find_element(By.CSS_SELECTOR, '#startTest')
    test_button.click()

    login_input = driver.find_element(By.CSS_SELECTOR, '#login')
    login_input.send_keys("Maria")

    password_input = driver.find_element(By.CSS_SELECTOR, '#password')
    password_input.send_keys("ssss")

    driver.find_element(By.CSS_SELECTOR, '#agree').click()

    driver.find_element(By.CSS_SELECTOR, '#register').click()

    driver.find_element(By.CSS_SELECTOR, '#loader')
    driver.implicitly_wait(10)

    success_message = driver.find_element(By.CSS_SELECTOR, '#successMessage')
    # driver.implicitly_wait(10)
    time.sleep(10)
    assert success_message.text == 'Вы успешно зарегистрированы!'

