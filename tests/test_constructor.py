import sys
import os

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from locators import MainPageLocators


class TestConstructorTabs:

    # Переход к разделу "Булки"
    def test_switch_to_bun_tab(self, driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)

        wait.until(EC.presence_of_element_located(MainPageLocators.INGREDIENTS_TITLE))

        # сначала переключаемся на «Начинки», чтобы затем проверить обратный переход на «Булки»
        filling_tab = wait.until(EC.element_to_be_clickable(MainPageLocators.FILLING_TAB))
        filling_tab.click()

        bun_tab = wait.until(EC.element_to_be_clickable(MainPageLocators.BUN_TAB))
        bun_tab.click()

        bun_section = driver.find_element(*MainPageLocators.BUN_SECTION)
        assert bun_section.is_displayed()


    # Переход к разделу "Соусы"
    def test_switch_to_sauce_tab(self, driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
    
        wait.until(EC.presence_of_element_located(MainPageLocators.INGREDIENTS_TITLE))
    
        sauce_tab = wait.until(EC.element_to_be_clickable(MainPageLocators.SAUCE_TAB))
        sauce_tab.click()
    
        sauce_section = driver.find_element(*MainPageLocators.SAUCE_SECTION)
        assert sauce_section.is_displayed()

    # Переход к разделу "Начинки"
    def test_switch_to_filling_tab(self, driver, base_url):
        driver.get(base_url)
        wait = WebDriverWait(driver, 10)
    
        wait.until(EC.presence_of_element_located(MainPageLocators.INGREDIENTS_TITLE))
    
        filling_tab = wait.until(EC.element_to_be_clickable(MainPageLocators.FILLING_TAB))
        filling_tab.click()
    
        filling_section = driver.find_element(*MainPageLocators.FILLING_SECTION)
        assert filling_section.is_displayed()
