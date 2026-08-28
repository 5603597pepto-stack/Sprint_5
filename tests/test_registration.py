import sys
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from locators import RegisterPageLocators
from constants import REGISTER_URL, LOGIN_ENDPOINT
from helpers import get_user_data


class TestRegistration:

    # Проверка успешной регистрации нового пользователя.
    def test_successful_registration(self, driver):

        driver.get(REGISTER_URL)

        user_data = get_user_data()

        WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegisterPageLocators.REGISTER_NAME_INPUT))

        driver.find_element(*RegisterPageLocators.REGISTER_NAME_INPUT).send_keys(user_data["name"])
        driver.find_element(*RegisterPageLocators.REGISTER_EMAIL_INPUT).send_keys(user_data["email"])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.url_contains(LOGIN_ENDPOINT))

        assert LOGIN_ENDPOINT in driver.current_url

    # Проверка ошибки при регистрации с некорректным (слишком коротким) паролем.
    def test_registration_invalid_password_error(self, driver):
      
        driver.get(REGISTER_URL)
        WebDriverWait(driver, 10).until(EC.presence_of_element_located(RegisterPageLocators.REGISTER_NAME_INPUT))

        user_data = get_user_data()
        user_data["password"] = "123"  # некорректный пароль — короче 6 символов

        driver.find_element(*RegisterPageLocators.REGISTER_NAME_INPUT).send_keys(user_data["name"])
        driver.find_element(*RegisterPageLocators.REGISTER_EMAIL_INPUT).send_keys(user_data["email"])
        driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
        driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()

        WebDriverWait(driver, 10).until(EC.visibility_of_element_located(RegisterPageLocators.PASSWORD_ERROR))
        error_message = driver.find_element(*RegisterPageLocators.PASSWORD_ERROR).text

        assert error_message == 'Некорректный пароль'
