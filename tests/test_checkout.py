import time

import pytest
from page_objects.checkout_page import CheckOutPage
from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage


@pytest.fixture(scope='function')
def execute_login_and_add_product(driver):
    login_page = LoginPage(driver)
    login_page.log_in_valid_user()
    product_page = ProductPage(driver)
    product_page.add_product_to_cart()


class TestCheckOut:
    # test is designed to check checkout flow (from adding product to cart to finishing the order)
    def test_check_out(self, driver, execute_login_and_add_product):
        product_page = ProductPage(driver)
        # get name of a random product on product page:
        product = product_page.get_inventory_name_by_index()
        # get price of a random product on product page:
        price = product_page.get_inventory_price_by_index()
        # open cart page:
        checkout_page = CheckOutPage(driver)
        checkout_page.open()
        # get name of the product in the cart:
        product_in_cart = checkout_page.get_item_name_in_cart()
        # get price of the product in the cart:
        price_in_cart = checkout_page.get_item_price_in_cart()
        # comparing names and prices on the product page and in the cart
        assert product == product_in_cart, "Wrong product is displayed in the cart"
        assert price == price_in_cart, "wrong price is displayed in the cart"
        # proceeding to checkout
        checkout_page.check_out()
        assert checkout_page.check_if_summary_visible(), "Summary is not visible"
        # proceeding to finalize the order
        checkout_page.click_finish()
        assert checkout_page.check_if_checkout_complete_visible(), "Checkout Complete Container is not visible"
