import sys
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from locators import MainPageLocators, PersonalAccountLocators
from constants import ACCOUNT_PROFILE_ENDPOINT, LOGIN_ENDPOINT, BASE_URL


class TestNavigation:

    # Переход в личный кабинет по клику на «Личный кабинет» в шапке
    def test_go_to_personal_account(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()

        wait.until(EC.url_contains(ACCOUNT_PROFILE_ENDPOINT))
        assert ACCOUNT_PROFILE_ENDPOINT in driver.current_url

    # Переход обратно в конструктор по клику на «Конструктор»
    def test_go_to_constructor_by_button(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        wait.until(EC.url_contains(ACCOUNT_PROFILE_ENDPOINT))

        driver.find_element(*MainPageLocators.CONSTRUCTOR_LINK).click()

        wait.until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/"

    # Переход обратно в конструктор по клику на логотип Stellar Burgers
    def test_go_to_constructor_by_logo(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        wait.until(EC.url_contains(ACCOUNT_PROFILE_ENDPOINT))

        driver.find_element(*MainPageLocators.LOGO).click()

        wait.until(EC.url_to_be(BASE_URL + "/"))
        assert driver.current_url == BASE_URL + "/"   

    # Выход из аккаунта по кнопке «Выйти» в личном кабинете
    def test_logout(self, driver, registered_user):
        wait = WebDriverWait(driver, 10)

        driver.find_element(*MainPageLocators.ACCOUNT_LINK).click()
        wait.until(EC.url_contains(ACCOUNT_PROFILE_ENDPOINT))

        logout_button = wait.until(EC.visibility_of_element_located(PersonalAccountLocators.LOGOUT_BUTTON))
        logout_button.click()

        wait.until(EC.url_contains(LOGIN_ENDPOINT))
        assert LOGIN_ENDPOINT in driver.current_url
