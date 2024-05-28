import random
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
import pytest
from selenium.common import StaleElementReferenceException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from page_objects.checkout_page import CheckOutPage
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

    # test is checking whether the number of items in the cart is increasing after pressing "add" for each product
    def test_add_all_products_to_cart(self, driver, execute_login):
        product_page = ProductPage(driver)
        expected_number = 0
        for add_button in product_page.get_buttons_list():
            add_button.click()
            expected_number += 1
        assert int(product_page._get_number_of_items_in_the_cart()) == expected_number, ("Wrong Number of Items in "
                                                                                             "the cart")
        product_page._go_to_cart()
        items = driver.find_elements(By.CLASS_NAME, "cart_item")
        item_to_keep_index = random.randint(0, len(items) - 1)
        item_to_keep = items[item_to_keep_index]
        item_to_keep_name = item_to_keep.find_element(By.CLASS_NAME,
                                                      "inventory_item_name").text

        for item in items:
            item_name = item.find_element(By.CLASS_NAME,
                                                  "inventory_item_name").text
            if item_to_keep_name != item_name:
                remove_button = item.find_element(By.XPATH,
                                              './/button[@class="btn btn_secondary btn_small cart_button"]')
                remove_button.click()
        remaining_items = driver.find_elements(By.CLASS_NAME, "cart_item")
        assert len(remaining_items) == 1, "More than one item remains in the cart."
        remaining_item_name = remaining_items[0].find_element(By.CLASS_NAME, "inventory_item_name").text
        assert remaining_item_name == item_to_keep_name, "The remaining item is not the expected one."
        checkout_page = CheckOutPage(driver)
        #RETURN TO PRODUCT PAGE
        # Verify that the button next to every item says "Add to cart" except for the item which was randomly selected
        checkout_page.press_continue_shopping()
        for item in product_page._get_item_list():
            item_in_product_page_name = item.find_element(By.CLASS_NAME,
                                          "inventory_item_name").text
            if item_to_keep_name != item_in_product_page_name:
                button = item.find_element(By.XPATH, './/button[@class="btn btn_primary btn_small btn_inventory "]')
                assert button.text == 'Add to cart', "Add to cart is not displayed"



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