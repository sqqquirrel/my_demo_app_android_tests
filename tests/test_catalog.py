import pytest
import allure
from pages.catalog_page import CatalogPage
from pages.product_page import ProductPage
from pages.components.menu_element import MenuElement
from test_data.products_data import PRODUCTS


@allure.feature("Catalog and Products")
class TestCatalog:

    @allure.title("Open catalog and verify it is displayed")
    def test_open_catalog(self, driver):
        with allure.step("Open menu"):
            menu = MenuElement(driver)
            menu.open_menu()

        with allure.step("Open catalog from menu"):
            menu.open_catalog()

        with allure.step("Verify catalog page is displayed"):
            catalog = CatalogPage(driver)
            assert catalog.is_page_displayed(catalog.PAGE_TITLE), "Catalog page is not displayed"

        first_product = PRODUCTS[0]["name"]
        with allure.step(f"Verify first product '{first_product}' is visible"):
            assert catalog.is_product_displayed(first_product), f"First product '{first_product}' is not visible"

    @pytest.mark.flaky(reruns=3, reruns_delay=3, message="Not stable product details opened")
    @allure.title("Open product details and verify name and price")
    @pytest.mark.parametrize("product", PRODUCTS)
    def test_product_details(self, driver, product):
        with allure.step("Open menu"):
            menu = MenuElement(driver)
            menu.open_menu()

        with allure.step("Open catalog from menu"):
            menu.open_catalog()

        catalog = CatalogPage(driver)
        with allure.step(f"Open product '{product['name']}' details"):
            catalog.open_product_by_name(product["name"])

        details = ProductPage(driver)
        with allure.step("Verify product name"):
            actual_name = details.get_product_name()
            assert product[
                       "name"] in actual_name, f"Product name mismatch: expected '{product['name']}', got '{actual_name}'"

        with allure.step("Verify product price"):
            actual_price = details.get_product_price()
            assert actual_price == product[
                "price"], f"Product price mismatch: expected '{product['price']}', got '{actual_price}'"

    @allure.title("Sort products by price ascending and verify order")
    def test_sort_by_price_ascending(self, driver):
        menu = MenuElement(driver)
        menu.open_menu()
        menu.open_catalog()
        catalog = CatalogPage(driver)

        with allure.step("Sort products by ascending price"):
            catalog.sort_by_price_asc()

        with allure.step("Get all product prices from catalog"):
            prices_text = catalog.get_all_prices()
            prices = [float(p.replace("$ ", "")) for p in prices_text]

        with allure.step("Verify prices are sorted ascending"):
            assert prices == sorted(prices), f"Products not sorted ascending: {prices}"
