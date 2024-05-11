from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    # product description:

    __dropdown = (By.CLASS_NAME, "product_sort_container")
    __prices = (By.CLASS_NAME, "inventory_item_price")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_inventory_items_prices(self):
        return super()._get_items_prices(self.__prices)

    def select_sort_from_drop_down(self, option: str):
        return super()._select_option_from_dropdown(self.__dropdown, option)
