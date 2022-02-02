import unittest
from selenium.common.exceptions import NoSuchElementException
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from mercadolibre.HomePage import HomePage
import time


class HomePageTest(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = webdriver.Chrome(executable_path=r'C:\\webdrivers\\chromedriver\\chromedriver.exe')
        driver = self.driver
        self.homepage = HomePage(self.driver)
        driver.get('https://www.mercadolibre.com.mx')
        self.homepage = HomePage(self.driver)
        driver.maximize_window()
        driver.implicitly_wait(15)

    def test_verify_home_page_elements(self):
        driver = self.driver
        self.homepage.is_homepage_header_elements_present()



    def test_search_gaming_mouse(self):
        driver = self.driver
        cookies_button = driver.find_element_by_id('newCookieDisclaimerButton')
        cookies_button.click()
        search_bar_css = 'input.nav-search-input'
        search_field = driver.find_element_by_css_selector(search_bar_css)
        search_field.click()
        search_field.clear()
        search_field.send_keys('Gaming mouse')
        search_field.submit()
        time.sleep(3)

        condition = driver.find_element(By.PARTIAL_LINK_TEXT, 'Nuevo')
        condition.click()
        time.sleep(3)

        full_shipping = driver.find_element_by_xpath(
            '/html/body/main/div/div[1]/aside/section/div[1]/ul/li/form/button')
        full_shipping.click()
        time.sleep(3)

        better_sellers = driver.find_element_by_css_selector('span.ui-search-filter-name')
        better_sellers.click
        time.sleep(3)

        order_by = driver.find_element_by_class_name('andes-dropdown__standalone-arrow').click()
        time.sleep(3)
        mayor_precio = driver.find_element_by_partial_link_text('Mayor precio')
        mayor_precio.click()

        articles = []
        prices = []

        for i in range(10):
            article_name = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[1]/section/ol/li[{i + 1}]/div/div/div[2]/div[1]/a[1]/h2').text
            articles.append(article_name)
            article_price = driver.find_element_by_xpath(f'//*[@id="root-app"]/div/div[1]/section/ol/li[{i + 1}]/div/div/div[2]/div[2]/div[1]/div[1]/div/div/div/span[1]/span[2]/span[2]').text
            prices.append(article_price)

        print(articles, prices)







    def tearDown(self) -> None:
        self.driver.close()



    if __name__ == '__main__':
        unittest.main(verbosity=2)
