import time
from selenium.webdriver.common.by import By
from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage


class TestProductSort:
    # test is designed to check whether the prices on the product page are sorted from low to high
    def test_sort_low_to_high(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_valid_user()
        product_page = ProductPage(driver)
        product_page.select_sort_from_drop_down('Price (low to high)')
        items_prices = product_page.get_inventory_items_prices()
        sorted_items_prices = items_prices.copy()
        sorted_items_prices.sort()
        assert items_prices == sorted_items_prices, "Prices are not sorted from low to high"

    # test is designed to check whether the prices on the product page are sorted from high to low
    def test_sort_high_to_low(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_valid_user()
        product_page = ProductPage(driver)
        product_page.select_sort_from_drop_down('Price (high to low)')
        items_prices = product_page.get_inventory_items_prices()
        sorted_items_prices = items_prices.copy()
        sorted_items_prices.sort()
        sorted_items_prices.reverse()
        assert items_prices == sorted_items_prices, "Prices are not sorted from high to low"
