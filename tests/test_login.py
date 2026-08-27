import sys
import os

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from locators import MainPageLocators, LoginPageLocators, RegisterPageLocators


class TestLogin:

    # вход по кнопке «Войти в аккаунт» на главной странице
    def test_login_from_login_button_main(self, driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

        login_button = wait.until(EC.element_to_be_clickable(MainPageLocators.LOGIN_BUTTON_MAIN))
        login_button.click()

        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    # вход через кнопку «Личный кабинет»
    def test_login_from_account_link(self, driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 5)
    
        account_link = wait.until(EC.element_to_be_clickable(MainPageLocators.ACCOUNT_LINK))
        account_link.click()

        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    # вход через кнопку в форме регистрации
    def test_login_from_login_link(self, driver, base_url):
        driver.get(f"{base_url}/register")
        wait = WebDriverWait(driver, 5)

        login_link = wait.until(EC.element_to_be_clickable(RegisterPageLocators.LOGIN_LINK))
        login_link.click()
            
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url

    # вход через кнопку в форме восстановления пароля
    def test_login_from_forgot_password_form(self, driver, base_url):
        driver.get(f"{base_url}/forgot-password")
        wait = WebDriverWait(driver, 10)
    
        login_link = wait.until(EC.element_to_be_clickable(LoginPageLocators.ACCOUNT_LINK_IN_FORGOT_PASSWORD))
        login_link.click()
    
        wait.until(EC.url_contains("/login"))
        assert "/login" in driver.current_url
