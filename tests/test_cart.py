import allure
from pages.catalog_page import CatalogPage
from pages.cart_page import CartPage
from pages.product_page import ProductPage
from test_data.products_data import PRODUCTS


@allure.feature("Cart")
@allure.story("Add products to cart and verify")
class TestCart:

    @allure.title("Add one product to cart and verify it appears")
    def test_add_one_product_to_cart(self, driver):
        catalog = CatalogPage(driver)
        product = PRODUCTS[0]

        with allure.step(f"Open product '{product['name']}' from catalog"):
            catalog.open_product_by_name(product["name"])

        details = ProductPage(driver)

        with allure.step("Click 'Add to Cart' button"):
            details.add_to_cart()

        with allure.step("Open cart"):
            catalog.menu.open_cart()

        cart = CartPage(driver)
        with allure.step("Verify product is in the cart with correct price"):
            cart_items = cart.get_cart_items()
            assert any(item[0] == product["name"] and item[1] == product["price"] for item in cart_items), \
                f"Product '{product['name']}' with price '{product['price']}' not found in cart"

        with allure.step("Verify cart count = 1"):
            count = catalog.menu.get_cart_item_count()
            assert count == 1, f"Expected cart count = 1, got {count}"
