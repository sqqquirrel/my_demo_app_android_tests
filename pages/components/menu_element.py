from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
import allure


class MenuElement(BasePage):
    """Side menu available on all screens."""
    APP_LOGO = (AppiumBy.ACCESSIBILITY_ID, "App logo and name")

    MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "View menu")
    CATALOG_BUTTON = (AppiumBy.XPATH,
                      '//android.widget.TextView[@resource-id="com.saucelabs.mydemoapp.android:id/itemTV" and @text="Catalog"]')
    LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")
    LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Logout Menu Item")
    CART_BUTTON = (AppiumBy.XPATH,
                   '//android.widget.RelativeLayout[@content-desc="Displays number of items in your cart"]/android.widget.ImageView')
    CART_ITEMS_COUNT = (
        AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.saucelabs.mydemoapp.android:id/cartTV"]')

    def __init__(self, driver):
        super().__init__(driver)
        assert self.is_element_visible(self.MENU_BUTTON), "Menu button not visible"

    @allure.step("Open side menu")
    def open_menu(self):
        """Opens the navigation menu"""
        self.click(*self.MENU_BUTTON)

    @allure.step("Open catalog from menu")
    def open_catalog(self):
        self.click(*self.CATALOG_BUTTON)

    @allure.step("Open cart from menu")
    def open_cart(self):
        self.click(*self.CART_BUTTON)

    @allure.step("Open login page from menu")
    def click_login(self):
        self.click(*self.LOGIN_BUTTON)

    @allure.step("Click logout in menu")
    def click_logout(self):
        self.click(*self.LOGOUT_BUTTON)

    def get_cart_item_count(self) -> int:
        """Return number of items displayed in cart icon (0 if empty)."""
        try:
            text = self.get_text(*self.CART_ITEMS_COUNT)
            return int(text) if text.isdigit() else 0
        except Exception:
            return 0

    def is_login_button_visible(self) -> bool:
        return self.is_element_visible(self.LOGIN_BUTTON)

    def is_logout_button_visible(self) -> bool:
        return self.is_element_visible(self.LOGOUT_BUTTON)

    def is_cart_button_visible(self) -> bool:
        return self.is_element_visible(self.CART_BUTTON)
