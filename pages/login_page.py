from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.components.menu_element import MenuElement


class LoginPage(BasePage):
    PAGE_TITLE = "Login"

    USERNAME = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/nameET')
    PASSWORD = (AppiumBy.ID, 'com.saucelabs.mydemoapp.android:id/passwordET')
    LOGIN_BTN = (AppiumBy.ACCESSIBILITY_ID, 'Tap to login with given credentials')
    ERROR_MESSAGE = (AppiumBy.ACCESSIBILITY_ID, "test-Error message")  # not released, upd. selector after fix

    def __init__(self, driver):
        super().__init__(driver)
        self.menu = MenuElement(driver)
        assert self.is_page_displayed(self.PAGE_TITLE), f"{self.PAGE_TITLE} page title is not displayed"

    def login(self, username, password):
        self.send_keys(*self.USERNAME, text=username)
        self.send_keys(*self.PASSWORD, text=password)
        self.click(*self.LOGIN_BTN)

    def get_error_message(self):
        try:
            return self.get_text(*self.ERROR_MESSAGE)
        except Exception as e:
            print(f"[WARN] No error message element found: {e}")
            return None
