from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    # product description:

    __dropdown = (By.CLASS_NAME, "product_sort_container")
    #__initial_prices = (By.CSS_SELECTOR, ".inventory_item_price")
    #__initial_prices_values = [float(price.text.replace("$", "")) for price in __initial_prices]
    __low_to_high = "Price (low to high)"

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_inventory_items_prices(self):
        return super()._get_items_prices("inventory_item_price")

    def select_from_drop_down(self):
        return super()._select_option_from_dropdown(self.__dropdown, self.__low_to_high)
