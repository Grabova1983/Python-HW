import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


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


def test_loading_website(driver, wait):
    driver.get('https://victoretc.github.io/selenium_waits/')
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, 'body > h1')))

    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#startTest')))

    test_button = driver.find_element(By.CSS_SELECTOR, '#startTest')
    test_button.click()

    login_input = driver.find_element(By.CSS_SELECTOR, '#login')
    login_input.send_keys("Maria")

    password_input = driver.find_element(By.CSS_SELECTOR, '#password')
    password_input.send_keys("ssss")

    driver.find_element(By.CSS_SELECTOR, '#agree').click()

    driver.find_element(By.CSS_SELECTOR, '#register').click()

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#loader')))

    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, '#successMessage')))

    success_message = driver.find_element(By.CSS_SELECTOR, '#successMessage')

    assert success_message.text == 'Вы успешно зарегистрированы!'

