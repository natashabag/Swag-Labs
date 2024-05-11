import time

from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage


class TestProductSort:
    def test_price_low_to_high(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_valid_user()
        product_page = ProductPage(driver)
        product_page.select_from_drop_down()
        items_prices = product_page.get_inventory_items_prices()
        sorted_items_prices = items_prices.copy()
        sorted_items_prices.sort()
        assert items_prices == sorted_items_prices, "Sorted Wrong"