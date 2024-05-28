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
    __inventory_item_name = (By.CLASS_NAME, "inventory_item_name")
    __inventory_item_price = (By.CLASS_NAME, "inventory_item_price")

    fake = Faker('en_US')
    __first_name = fake.first_name()
    __last_name = fake.last_name()
    __zip_code = '92021'

    __remove_button = (By.CLASS_NAME, "btn btn_secondary btn_small cart_button")
    __continue_shopping_button = (By.ID, "continue-shopping")

    __error_message = (By.XPATH, '//h3[@data-test="error"]')
    __total_price = (By.XPATH, '//div[@class="summary_subtotal_label"]')
    __tax = (By.XPATH, '//div[@class="summary_tax_label"]')

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def open(self):
        super()._open_url(self.__url)

    def fill_out_check_out_form(self):
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

    def get_item_name_in_cart(self):
        return super()._get_text(self.__inventory_item_name)

    def get_item_price_in_cart(self):
        return float(super()._get_text(self.__inventory_item_price).replace('$', ''))

    def get_remove_buttons_list(self):
        return super()._find_elements(self.__remove_button)

    def press_continue_shopping(self):
        super()._click(self.__continue_shopping_button)

    def press_checkout_button(self):
        super()._click(self.__checkout_button)

    def press_continue_button(self):
        super()._click(self.__continue_button)

    def get_error_message(self):
        return super()._get_text(self.__error_message)

    def fill_out_name(self):
        super()._type(self.__first_name_field, self.__first_name)

    def fill_out_last_name(self):
        super()._type(self.__last_name_field, self.__last_name)

    def get_total_price(self):
        total_price_str = super()._get_text(self.__total_price)
        price_str = total_price_str.split('$')[1].strip()
        total_price_number = float(price_str)
        return total_price_number
    def get_tax(self):
        full_tax_str = super()._get_text(self.__tax)
        tax_str = full_tax_str.split('$')[1].strip()
        tax = float(tax_str)
        return tax

