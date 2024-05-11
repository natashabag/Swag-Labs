import time
from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage


class TestLoginPage:
    def test_valid_user(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_valid_user()
        product_page = ProductPage(driver)
        assert product_page.expected_url == product_page.current_url, "Actual URL is not the same as expected"

    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_locked_out_user()
        assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out.", ("Wrong Error "
                                                                                                         "message")