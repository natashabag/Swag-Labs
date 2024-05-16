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
        checkout_page = CheckOutPage(driver)
        checkout_page.open()
        checkout_page.check_out()
        assert checkout_page.check_if_summary_visible(), "Summary is not visible"
        checkout_page.click_finish()
        assert checkout_page.check_if_checkout_complete_visible(), "Checkout Complete Container is not visible"
