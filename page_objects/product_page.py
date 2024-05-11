from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver

from page_objects.base_page import BasePage


class ProductPage(BasePage):
    # product description:
    __url = "https://www.saucedemo.com/inventory.html"
    __dropdown = (By.CLASS_NAME, "product_sort_container")

    def __init__(self, driver: WebDriver):
        super().__init__(driver)

    def get_inventory_items_prices(self):
        items_prices = []
        for item_price in self._driver.find_elements(By.CLASS_NAME, "inventory_item_price"):
            only_numbers = item_price.text.replace('$', '')
            items_prices.append(float(only_numbers))
        return items_prices

    def get_inventory_names(self):
        items_names = []
        for item_name in self._driver.find_elements(By.CLASS_NAME, "inventory_item_name"):
            items_names.append(item_name.text)
        return items_names


    def select_sort_from_drop_down(self, option: str):
        return super()._select_option_from_dropdown(self.__dropdown, option)

    @property
    def current_url(self) -> str:
        return self._driver.current_url

    @property
    def expected_url(self) -> str:
        return self.__url
