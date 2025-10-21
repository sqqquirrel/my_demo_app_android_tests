from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class ProductPage(BasePage):
    PAGE_TITLE = "Product Highlights"
    TITLE = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/productTV')
    PRICE = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/priceTV')
    ADD_TO_CART = (AppiumBy.ACCESSIBILITY_ID, 'Tap to add product to cart')

    def __init__(self, driver):
        super().__init__(driver)
        assert self.is_page_displayed(self.PAGE_TITLE), f"{self.PAGE_TITLE} is not displayed"

    def add_to_cart(self):
        self.click(*self.ADD_TO_CART)

    def get_product_name(self):
        return self.get_text(*self.TITLE)

    def get_product_price(self):
        return self.get_text(*self.PRICE)
