import time

from page_objects.login_page import LoginPage


class TestLoginPage:
    def test_valid_user(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_valid_user()
        time.sleep(5)

    def test_locked_out_user(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in_locked_out_user()
        assert login_page.get_error_message() == "Epic sadface: Sorry, this user has been locked out.", ("Wrong Error "
                                                                                                         "message")