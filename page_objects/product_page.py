import random
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from page_objects.base_page import BasePage


class ProductPage(BasePage):
    # product description:
    __url = "https://www.saucedemo.com/inventory.html"
    __dropdown = (By.CLASS_NAME, "product_sort_container")
    __shopping_cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    __price = (By.CLASS_NAME, "inventory_item_price")
    __inventory_name = (By.CLASS_NAME, "inventory_item_name")
    __index = random.randint(0, 5)
    __add_button = (By.XPATH, '//div[@class="inventory_item"]//button')
    __burger_menu = (By.ID, "react-burger-menu-btn")
    __logout_button = (By.ID, "logout_sidebar_link")
    __inventory_item = (By.CLASS_NAME, "inventory_item")
    __item = (By.ID, "inventory_item")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_inventory_items_prices(self):
        items_prices = []
        for item_price in super()._find_elements(self.__price):
            only_numbers = item_price.text.replace('$', '')
            items_prices.append(float(only_numbers))
        return items_prices

    def get_inventory_names(self):
        items_names = []
        for item_name in super()._find_elements(self.__inventory_name):
            items_names.append(item_name.text)
        return items_names

    def get_buttons_list(self):
        return super()._find_elements(self.__add_button)

    def get_inventory_name_by_index(self):
        return self.get_inventory_names()[self.__index]

    def get_inventory_price_by_index(self):
        return self.get_inventory_items_prices()[self.__index]

    def select_sort_from_drop_down(self, option: str):
        return super()._select_option_from_dropdown(self.__dropdown, option)

    def add_product_to_cart(self):
        self.get_buttons_list()[self.__index].click()

    def _get_number_of_items_in_the_cart(self):
        return super()._get_text(self.__shopping_cart_badge)

    def _logout(self):
        super()._click(self.__burger_menu)
        super()._click(self.__logout_button)

    def _get_product_cards(self):
        product_cards = super()._find_elements(self.__inventory_item)
        return product_cards

    def _go_to_cart(self):
        super()._click(self.__shopping_cart_badge)

    def _get_item_list(self):
        return super()._find_elements(self.__inventory_item)



    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self.__url
