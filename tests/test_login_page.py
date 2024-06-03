from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage


class TestLoginPage:
    # test is designed to check whether valid user can log in
    def test_valid_user(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_valid_user()
        product_page = ProductPage(driver)
        assert product_page.expected_url == product_page.current_url, "Actual URL is not the same as expected"

    # test is designed to check whether a locked out user can log in
    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_locked_out_user()
        assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out.", ("Wrong Error "
                                                                                                         "message")

    # test is designed to check whether a user can log in without password
    def test_login_without_password(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_without_password()
        assert login_page.get_error_message() == "Epic sadface: Password is required", "Wrong Error Message"

    # test is designed to check whether a user can log in without username
    def test_login_without_username(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_without_username()
        assert login_page.get_error_message() == "Epic sadface: Username is required", "Wrong Error Message"

    # test is designed to check whether a user can log in with wrong password
    def test_login_with_wrong_password(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_with_wrong_password()
        assert login_page.get_error_message() == ("Epic sadface: Username and password do not match any user in this "
                                                  "service")

    # test is designed to check whether a user can log in with invalid username
    def test_login_with_invalid_username(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_with_invalid_username()
        assert login_page.get_error_message() == ("Epic sadface: Username and password do not match any user in this "
                                                  "service")