from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class CheckOutPage(BasePage):
    __url = "https://www.saucedemo.com/cart.html"
    __first_name_field = (By.ID, "first-name")
    __last_name_field = (By.ID, "last-name")
    __zip_field = (By.ID, "postal-code")
    __checkout_button = (By.ID, "checkout")
    __continue_button = (By.ID, "continue")
    __summary_info = (By.CLASS_NAME, "summary_info")
    __finish_button = (By.ID, "finish")
    __checkout_complete_container = (By.ID, "checkout_complete_container")

    fake = Faker('en_US')
    __first_name = fake.first_name()
    __last_name = fake.last_name()
    __zip_code = '92021'

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def check_out(self):
        super()._click(self.__checkout_button)
        super()._type(self.__first_name_field, self.__first_name)
        super()._type(self.__last_name_field, self.__last_name)
        super()._type(self.__zip_field, self.__zip_code)
        super()._click(self.__continue_button)

    def click_finish(self):
        super()._click(self.__finish_button)

    def check_if_summary_visible(self):
        return super()._is_visible(self.__summary_info)

    def check_if_checkout_complete_visible(self):
        return super()._is_visible(self.__checkout_complete_container)
