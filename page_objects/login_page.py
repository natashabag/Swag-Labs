from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://www.saucedemo.com/"

    # login fields:
    __username_field = (By.ID, "user-name")
    __password_field = (By.ID, "password")
    __login_button = (By.ID, "login-button")

    # credentials:
    __username = "standard_user"
    __password = "secret_sauce"
    __locked_out_username = "locked_out_user"

    # error message:
    __error_message_container = (By.CSS_SELECTOR, 'h3[data-test="error"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def log_in_valid_user(self):
        super()._open_url(self.__url)
        super()._type(self.__username_field, self.__username)
        super()._type(self.__password_field, self.__password)
        super()._click(self.__login_button)

    def log_in_locked_out_user(self):
        super()._open_url(self.__url)
        super()._type(self.__username_field, self.__locked_out_username)
        super()._type(self.__password_field, self.__password)
        super()._click(self.__login_button)

    def log_in_without_password(self):
        super()._open_url(self.__url)
        super()._type(self.__username_field, self.__username)
        super()._click(self.__login_button)

    def log_in_without_username(self):
        super()._open_url(self.__url)
        super()._type(self.__password_field, self.__password)
        super()._click(self.__login_button)

    def get_error_message(self):
        return super()._get_text(self.__error_message_container)

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self.__url



