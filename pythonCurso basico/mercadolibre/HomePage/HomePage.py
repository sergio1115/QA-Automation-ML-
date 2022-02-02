from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class HomePage(object):

    def __init__(self, driver):
        self.driver = driver
        self.url = 'https://www.mercadolibre.com'

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by=how, value=what)
        except NoSuchElementException as variable:
            return False
        return True

    @property
    def is_loaded(self):
        WebDriverWait(self.driver).until(EC.presence_of_element_located(By.CLASS_NAME, 'ml-site-list'))
        return True

    @property
    def accept_cookies_button(self):
        cookies_button = self.driver.find_element_by_id('newCookieDisclaimerButton')
        cookies_button.click()
        return True

    @property
    def keyword(self):
        search_bar = 'input.nav-search-input'
        search_field = self.driver.find_element_by_css_selector(search_bar)
        return search_field.get_attribute('value)')

    def type_search(self, keyword):
        search_bar = 'input.nav-search-input'
        search_field = self.driver.find_element_by_css_selector(search_bar)
        search_field.send_keys(keyword)

    def submit_click(self):
        submit_locator = 'button.nav-search-btn'
        submit_button = self.driver.find_element_by_css_selector(submit_locator)
        submit_button.click()

    def is_homepage_header_elements_present(self, ):
        tc = unittest.TestCase('__init__')

        # HomepageLocators
        logo_css = 'a.nav-logo'
        search_bar_CSS = 'input.nav-search-input'
        menu_CSS = 'div.nav-header-menu-wrapper'
        shopping_car_CSS = 'i.nav-icon-cart'
        Postal_code = 'a.nav-menu-cp.nav-menu-cp-logged'
        categories_CSS = 'a.nav-menu-categories-link'
        offers_Xpath = '/html/body/header/div/div[2]/ul/li[3]/a'
        history_xpath = '/html/body/header/div/div[2]/ul/li[4]/a'
        super_market = '/html/body/header/div/div[2]/ul/li[5]/a'
        fashion = '/html/body/header/div/div[2]/ul/li[6]/a'
        sell = "/html/body/header/div/div[2]/ul/li[7]/a"
        help = "/html/body/header/div/div[2]/ul/li[8]/a"
        create_account = "nav#nav-header-menu > a[data-link-id = registration]"
        login = "nav#nav-header-menu > a[data-link-id = login]"
        purchases = "nav#nav-header-menu > a[data-link-id = purchases]"

        tc.assertTrue(self.is_element_present(By.CSS_SELECTOR, logo_css))
        tc.assertTrue(self.is_element_present(By.CSS_SELECTOR, search_bar_CSS))
        tc.assertTrue(self.is_element_present(By.CSS_SELECTOR, menu_CSS))
        tc.assertTrue(self.is_element_present(By.CSS_SELECTOR, shopping_car_CSS))
        tc.assertTrue(self.is_element_present(By.CSS_SELECTOR, Postal_code))
        tc.assertTrue(self.is_element_present(By.CSS_SELECTOR, categories_CSS))
        tc.assertTrue(self.is_element_present(By.XPATH, offers_Xpath))
        tc.assertTrue(self.is_element_present(By.XPATH, history_xpath))
        tc.assertTrue(self.is_element_present(By.XPATH, super_market))
        tc.assertTrue(self.is_element_present(By.XPATH, fashion))
        tc.assertTrue(self.is_element_present(By.XPATH, sell))
        tc.assertTrue(self.is_element_present(By.XPATH, help))
        tc.assertTrue(self.is_element_present(By.CSS_SELECTOR, create_account))
        tc.assertTrue(self.is_element_present(By.CSS_SELECTOR, login))
        tc.assertTrue(self.is_element_present(By.CSS_SELECTOR, purchases))
