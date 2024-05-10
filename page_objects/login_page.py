from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class LoginPage(BasePage):
    __url = "https://www.saucedemo.com/"
    __username_field = (By.ID, "user-name")
    __password_field = (By.ID, "password")
    __login_button = (By.ID, "login-button")

    #credentials:
    __username = "standard_user"
    __password = "secret_sauce"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def log_in(self):
        super()._open_url(self.__url)
        super()._type(self.__username_field, self.__username)
        super()._type(self.__password_field, self.__password)
        super()._click(self.__login_button)
