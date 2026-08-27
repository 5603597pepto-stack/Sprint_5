import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from generate_credentials import generate_email, generate_password
from locators import RegisterPageLocators, LoginPageLocators


BASE_URL = "https://stellarburgers.education-services.ru"
@pytest.fixture
def base_url():
    return BASE_URL


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


@pytest.fixture
def user_data():
    return {
        "name": "Анна",
        "email": generate_email(),
        "password": generate_password(),
    }


@pytest.fixture
def registered_user(driver, base_url, user_data):
    driver.get(f"{base_url}/register")
    wait = WebDriverWait(driver, 10)
    wait.until(expected_conditions.presence_of_element_located(RegisterPageLocators.REGISTER_NAME_INPUT))

    driver.find_element(*RegisterPageLocators.REGISTER_NAME_INPUT).send_keys(user_data["name"])
    driver.find_element(*RegisterPageLocators.REGISTER_EMAIL_INPUT).send_keys(user_data["email"])
    driver.find_element(*RegisterPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
    driver.find_element(*RegisterPageLocators.REGISTER_BUTTON).click()
    wait.until(expected_conditions.url_contains("/login"))

    driver.find_element(*LoginPageLocators.EMAIL_INPUT).send_keys(user_data["email"])
    driver.find_element(*LoginPageLocators.PASSWORD_INPUT).send_keys(user_data["password"])
    driver.find_element(*LoginPageLocators.LOGIN_BUTTON).click()
    wait.until(expected_conditions.url_contains("/"))

    return user_data
    