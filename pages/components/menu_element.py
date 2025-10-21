# from appium.webdriver.common.appiumby import AppiumBy
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
#
# from pages.base_page import BasePage
#
#
# class MenuElement:
#     APP_LOGO = (AppiumBy.ACCESSIBILITY_ID, "App logo and name")
#     MENU_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "View menu")
#     CATALOG_BUTTON = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.saucelabs.mydemoapp.android:id/itemTV" and @text="Catalog"]')
#     LOGIN_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Login Menu Item")
#     LOGOUT_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "Logout Menu Item")
#     CART_BUTTON = (AppiumBy.XPATH, '//android.widget.RelativeLayout[@content-desc="Displays number of items in your cart"]/android.widget.ImageView')
#     CART_ITEMS_COUNT = (AppiumBy.XPATH, '//android.widget.TextView[@resource-id="com.saucelabs.mydemoapp.android:id/cartTV"]')
#
#     def __init__(self, driver, timeout=10):
#         self.page = BasePage(driver)
#         self.driver = driver
#
#         assert self.is_menu_button_visible(timeout), "Menu button is not visible"
#
#     def is_menu_button_visible(self, timeout=10) -> bool:
#         try:
#             WebDriverWait(self.driver, timeout).until(
#                 EC.visibility_of_element_located(self.MENU_BUTTON)
#             )
#             return True
#         except Exception:
#             return False
#
#     def open_menu(self):
#         self.page.click(*self.MENU_BUTTON)
#
#     def open_catalog(self):
#         self.page.click(*self.CATALOG_BUTTON)
#
#     def click_login(self):
#         self.open_menu()
#         self.page.click(*self.LOGIN_BUTTON)
#
#     def click_logout(self):
#         self.open_menu()
#         self.page.click(*self.LOGOUT_BUTTON)
#
#     def open_cart(self):
#         self.page.click(*self.CART_BUTTON)
#
#     def is_login_button_visible(self) -> bool:
#         try:
#             self.open_menu()
#             self.page.find(*self.LOGIN_BUTTON)
#             return True
#         except Exception:
#             return False
#
#     def is_logout_button_visible(self) -> bool:
#         try:
#             self.open_menu()
#             self.page.find(*self.LOGOUT_BUTTON)
#             return True
#         except Exception:
#             return False
#
#     def get_cart_items_count(self) -> int:
#         count_text = self.page.find(*self.CART_ITEMS_COUNT).text
#         try:
#             return int(count_text)
#         except ValueError:
#             return 0


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

    # ---------- Core interactions ----------

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

    # ---------- States ----------

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
