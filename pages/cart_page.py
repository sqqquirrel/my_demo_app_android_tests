from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage

class CartPage(BasePage):
    PAGE_TITLE = "My Cart"

    CART_ITEM_TITLE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/titleTV")
    CART_ITEM_PRICE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/priceTV")

    def __init__(self, driver):
        super().__init__(driver)
        assert self.is_page_displayed(self.PAGE_TITLE), f"{self.PAGE_TITLE} is not displayed"

    def get_cart_items(self):
        titles = [el.text for el in self.driver.find_elements(*self.CART_ITEM_TITLE)]
        prices = [el.text for el in self.driver.find_elements(*self.CART_ITEM_PRICE)]
        return list(zip(titles, prices))