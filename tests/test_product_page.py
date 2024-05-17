import pytest
from selenium.webdriver.common.by import By

from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage


@pytest.fixture(scope='function')
def execute_login(driver):
    login_page = LoginPage(driver)
    login_page.log_in_valid_user()


class TestProductPage:
    # test is designed to check whether user can add product to cart
    def test_random_product_to_cart(self, driver, execute_login):
        product_page = ProductPage(driver)
        product_page.add_product_to_cart()
        assert product_page._get_number_of_items_in_the_cart() == '1', "Wrong Number of Items in the cart"

    # test is designed to check whether user can successfully log out
    def test_logging_out(self, driver, execute_login):
        product_page = ProductPage(driver)
        product_page._logout()
        login_page = LoginPage(driver)
        assert login_page.expected_url == login_page.current_url, "User is redirected to the wrong page"

    # test is designed to check whether product cards contain necessary information after user logs in
    def test_everything_is_displayed(self, driver, execute_login):
        product_page = ProductPage(driver)
        for card in product_page._get_product_cards():
            # Check for the presence of the name
            name = card.find_element(By.CLASS_NAME, "inventory_item_name")
            assert name is not None and name.text != "", "Product name is missing"
            # Check for the presence of the price
            price = card.find_element(By.CLASS_NAME, "inventory_item_price")
            price_in_numbers = price.text.replace('$', '')
            assert price is not None and price.text != "", "Product price is missing"
            # Check price range is between $6 and $50
            assert 6 < float(price_in_numbers) < 50, "wrong price"
            # Check for the presence of the picture
            picture = card.find_element(By.CLASS_NAME, "inventory_item_img")
            assert picture is not None and picture.get_attribute("src") != "", "Product picture is missing"