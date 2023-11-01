import time

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
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#content > div > button')))
    driver.find_element(By.CSS_SELECTOR,'#content > div > button').click()
    # time.sleep(2)
    wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '#elements > .added-manually')))
    delete_button = driver.find_element(By.CSS_SELECTOR, '#elements > .added-manually')
    delete_button.click()
    # time.sleep(2)
    assert not delete_button.isDisplayed
