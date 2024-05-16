from typing import List

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.select import Select


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)
        self.url = url

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _find_elements(self, locator: tuple) -> List[WebElement]:
        return self._driver.find_elements(*locator)

    def _click(self, locator: tuple):
        self._find(locator).click()

    def _type(self, locator: tuple, text: str):
        self._find(locator).send_keys(text)

    def _get_text(self, locator: tuple) -> str:
        return self._find(locator).text

    def _select_option_from_dropdown(self, locator, text):
        select_element = self._find(locator)
        select = Select(select_element)
        select.select_by_visible_text(text)

    def _is_visible(self, locator):
        return self._find(locator).is_displayed()
