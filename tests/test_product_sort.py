import time

from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage


class TestProductSort:
    def test_product_sort(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_valid_user()
        product_page = ProductPage(driver)
        time.sleep(10)
        product_page.select_from_drop_down()
        time.sleep(5)