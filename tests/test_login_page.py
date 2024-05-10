import time

from page_objects.login_page import LoginPage


class TestLoginPage:
    def test_alert_page_accept(self, driver):
        login_page = LoginPage(driver)
        login_page.log_in()
        time.sleep(5)