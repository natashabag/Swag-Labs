import random
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class CheckOutPage(BasePage):
    __url = "https://www.saucedemo.com/cart.html"
    # check out fields:
    __first_name_field = (By.ID, "first-name")
    __last_name_field = (By.ID, "last-name")
    __zip_field = (By.ID, "postal-code")
    __checkout_button = (By.ID, "checkout")
    __continue_button = (By.ID, "continue")
    __summary_info = (By.CLASS_NAME, "summary_info")

    # customer credentials:
    fake = Faker('en_US')
    __first_name = fake.first_name()
    __last_name = fake.last_name()
    __zip_code = '92021'

    # check out flow buttons:
    __finish_button = (By.ID, "finish")
    __checkout_complete_container = (By.ID, "checkout_complete_container")
    __continue_shopping_button = (By.ID, "continue-shopping")
    __remove_button = (By.XPATH, './/button[@class="btn btn_secondary btn_small cart_button"]')

    # item description:
    __inventory_item_name = (By.CLASS_NAME, "inventory_item_name")
    __inventory_item_price = (By.CLASS_NAME, "inventory_item_price")
    __cart_item = (By.CLASS_NAME, "cart_item")

    # price:
    __total_price_without_tax = (By.XPATH, '//div[@class="summary_subtotal_label"]')
    __tax = (By.XPATH, '//div[@class="summary_tax_label"]')
    __total_price = (By.XPATH, '//div[@class="summary_total_label"]')

    # other:
    __error_message = (By.XPATH, '//h3[@data-test="error"]')

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

    def get_price_without_tax(self):
        price_without_tax_full_str = super()._get_text(self.__total_price_without_tax)
        price_without_tax_str = price_without_tax_full_str.split('$')[1].strip()
        price_without_tax = float(price_without_tax_str)
        return price_without_tax

    def get_tax(self):
        # getting string containing tax information:
        full_tax_str = super()._get_text(self.__tax)
        # splitting string to only get numbers after $:
        tax_str = full_tax_str.split('$')[1].strip()
        # converting string to number
        tax = float(tax_str)
        return tax

    def get_total_price(self):
        # getting string containing total price information:
        total_price_str = super()._get_text(self.__total_price)
        # splitting string to only get numbers after $:
        total_price_str = total_price_str.split('$')[1].strip()
        # converting string to number
        total_price = float(total_price_str)
        return total_price

    def remove_all_but_one_random_item_from_cart(self):
        # get all items in the cart:
        items = super()._find_elements(self.__cart_item)
        # randomly select an item to keep
        item_to_keep_index = random.randint(0, len(items) - 1)
        item_to_keep = items[item_to_keep_index]
        item_to_keep_name = item_to_keep.find_element(*self.__inventory_item_name).text
        # remove all items except the randomly selected one
        for item in items:
            item_name = item.find_element(*self.__inventory_item_name).text
            if item_to_keep_name != item_name:
                remove_button = item.find_element(*self.__remove_button)
                remove_button.click()
        # return randomly selected item's name to assert in the future test
        return item_to_keep_name
