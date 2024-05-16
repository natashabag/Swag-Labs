import pytest
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

    def test_logging_out(self, driver, execute_login):
        product_page = ProductPage(driver)
        product_page._logout()
        login_page = LoginPage(driver)
        assert login_page.expected_url == login_page.current_url, "User is redirected to the wrong page"

