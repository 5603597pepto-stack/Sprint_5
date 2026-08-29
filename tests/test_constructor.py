import sys
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from locators import MainPageLocators
from constants import BASE_URL


class TestConstructorTabs:

    # Переход к разделу "Булки"
    def test_switch_to_bun_tab(self, driver):
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(MainPageLocators.INGREDIENTS_TITLE))

        # сначала переключаемся на «Начинки», чтобы затем проверить обратный переход на «Булки»
        driver.find_element(*MainPageLocators.FILLING_TAB).click()

        bun_tab = driver.find_element(*MainPageLocators.BUN_TAB)
        bun_tab.click()

        assert wait.until(
        lambda d: "tab_type_current" in d.find_element(*MainPageLocators.BUN_SECTION).get_attribute("class"))


    # Переход к разделу "Соусы"
    def test_switch_to_sauce_tab(self, driver):
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(MainPageLocators.INGREDIENTS_TITLE))
    
        sauce_tab = driver.find_element(*MainPageLocators.SAUCE_TAB)
        sauce_tab.click()
    
        assert wait.until(
        lambda d: "tab_type_current" in d.find_element(*MainPageLocators.SAUCE_SECTION).get_attribute("class"))

    # Переход к разделу "Начинки"
    def test_switch_to_filling_tab(self, driver):
        driver.get(BASE_URL)

        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located(MainPageLocators.INGREDIENTS_TITLE))
    
        filling_tab = wait.until(EC.element_to_be_clickable(MainPageLocators.FILLING_TAB))
        filling_tab.click()

        assert wait.until(
        lambda d: "tab_type_current" in d.find_element(*MainPageLocators.FILLING_SECTION).get_attribute("class"))
    