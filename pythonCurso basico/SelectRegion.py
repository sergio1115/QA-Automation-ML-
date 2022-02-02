# libraries

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.expected_conditions import NoSuchElementException
from selenium.webdriver.support import expected_conditions


class SelectRegion(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r'C:\\webdrivers\\chromedriver\\chromedriver.exe')
        driver = self.driver
        driver.get('https://www.mercadolibre.com')
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_selecting_region(self):
        driver = self.driver
        driver.find_element(By.CSS_SELECTOR, 'a#MX').click()
        driver.implicitly_wait(5)
        get_title = driver.title
        self.assertTrue(get_title, driver.title)

    def tearDown(self) -> None:
        self.driver.close()

    def is_element_present(self, how, what):
        try:
            self.driver.find_element(by = how, value = what)
        except NoSuchElementException as variable:
            return False
        return True

    if __name__ == "__main__":
        unittest.main()