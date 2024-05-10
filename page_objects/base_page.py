from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BasePage:
    def __init__(self, driver: WebDriver):
        self._driver = driver

    def _open_url(self, url: str):
        self._driver.get(url)
        self.url = url

    def _find(self, locator: tuple) -> WebElement:
        return self._driver.find_element(*locator)

    def _click(self, locator: tuple):
        self._find(locator).click()

    def _type(self, locator: tuple, text: str):
        self._find(locator).send_keys(text)

    def _get_text(self, locator: tuple) -> str:
        return self._find(locator).text