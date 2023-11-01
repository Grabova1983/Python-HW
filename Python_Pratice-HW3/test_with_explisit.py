from selenium.webdriver.support import expected_conditions as EC
from data import START_PAGE
from locators import TITLE, START_TEST_BUTTON, LOGIN, PASSWORD, CHECKBOX_AGREE, REGISTER_BUTTON, LOADER, SUCCESS_MESSAGE


def test_loading_website(driver, wait, fake_email):
    driver.get(START_PAGE)
    title = wait.until(EC.visibility_of_element_located(TITLE))
    assert title.text == 'Практика с ожиданиями в Selenium'

    test_button = wait.until(EC.element_to_be_clickable(START_TEST_BUTTON))
    test_button.click()

    login_input = wait.until(EC.visibility_of_element_located(LOGIN))
    login_input.clear()
    login_input.send_keys(fake_email)

    password_input = wait.until(EC.visibility_of_element_located(PASSWORD))
    password_input.clear()
    password_input.send_keys(fake_email)

    checkbox = wait.until(EC.visibility_of_element_located(CHECKBOX_AGREE))
    checkbox.click()
    assert checkbox.is_selected() == True

    register_button = wait.until(EC.visibility_of_element_located(REGISTER_BUTTON))
    register_button.click()

    wait.until(EC.visibility_of_element_located(LOADER))

    success_message = wait.until(EC.visibility_of_element_located(SUCCESS_MESSAGE))

    assert success_message.text == 'Вы успешно зарегистрированы!'

