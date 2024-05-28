import pytest
from page_objects.checkout_page import CheckOutPage
from page_objects.login_page import LoginPage
from page_objects.product_page import ProductPage


@pytest.fixture(scope='function')
def execute_login(driver):
    login_page = LoginPage(driver)
    login_page.log_in_valid_user()


@pytest.fixture(scope='function')
def add_product(driver):
    product_page = ProductPage(driver)
    product_page.add_product_to_cart()


class TestCheckOut:
    # test is designed to check checkout flow (from adding product to cart to finishing the order)
    def test_check_out(self, driver, execute_login, add_product):
        product_page = ProductPage(driver)
        # get name of a random product on product page:
        product = product_page.get_inventory_name_by_index()
        # get price of a random product on product page:
        price = product_page.get_inventory_price_by_index()
        # open cart page:
        checkout_page = CheckOutPage(driver)
        checkout_page.open()
        # get name of the product in the cart:
        product_in_cart = checkout_page.get_item_name_in_cart()
        # get price of the product in the cart:
        price_in_cart = checkout_page.get_item_price_in_cart()
        # comparing names and prices on the product page and in the cart
        assert product == product_in_cart, "Wrong product is displayed in the cart"
        assert price == price_in_cart, "Wrong price is displayed in the cart"
        # proceeding to checkout
        checkout_page.fill_out_check_out_form()
        assert checkout_page.check_if_summary_visible(), "Summary is not visible"
        # proceeding to finalize the order
        checkout_page.click_finish()
        assert checkout_page.check_if_checkout_complete_visible(), "Checkout Complete Container is not visible"

    """test is designed to check checkout flow and verify whether user can check out without entering First Name, 
    Last Name and Zip """

    def test_check_out_negative(self, driver, execute_login):
        product_page = ProductPage(driver)
        # adding all products to cart
        product_page._add_all_items_to_cart()
        # proceeding to checkout:
        product_page._go_to_cart()
        checkout_page = CheckOutPage(driver)
        checkout_page.press_checkout_button()
        checkout_page.press_continue_button()
        # verifying that user cannot continue checking out without entering first name
        assert checkout_page.get_error_message() == "Error: First Name is required", "Wrong Error Message"
        checkout_page.fill_out_name()
        checkout_page.press_continue_button()
        # verifying that user cannot continue checking out without entering last name
        assert checkout_page.get_error_message() == "Error: Last Name is required", "Wrong Error Message"
        checkout_page.fill_out_last_name()
        checkout_page.press_continue_button()
        # verifying that user cannot continue checking out without entering zip code
        assert checkout_page.get_error_message() == "Error: Postal Code is required", "Wrong Error Message"

    def test_check_total_amount(self, driver, execute_login):
        product_page = ProductPage(driver)
        # adding all products to cart
        product_page._add_all_items_to_cart()
        # getting prices for all products on product page
        inventory_items_prices = product_page.get_inventory_items_prices()
        # getting sum of all prices for all products on product page
        total_items_price = sum(inventory_items_prices)
        # getting expected tax for all products on product page
        expected_tax = round(total_items_price * 0.08, 2)
        expected_total_price = total_items_price + expected_tax
        # proceeding to checkout
        product_page._go_to_cart()
        checkout_page = CheckOutPage(driver)
        checkout_page.fill_out_check_out_form()
        # verifying that total amount in the order summary matches the sum of all prices for all products on product
        # page
        assert checkout_page.get_price_without_tax() == total_items_price, (
            "Prices on the product page and prices in the "
            "order summary don't much")
        # verifying that tax in the order summary matches the expected tax (8%)
        assert checkout_page.get_tax() == expected_tax, "Expected tax does not match tax in the product summary"
        # verifying that tax in the order summary matches the expected tax (8%) + the sum of all prices for all
        # products on product page
        assert checkout_page.get_total_price() == expected_total_price, ("Expected total price does not "
                                                                         "match total in the product "
                                                                         "summary")
