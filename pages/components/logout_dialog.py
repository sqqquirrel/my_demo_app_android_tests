from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage


class LogoutDialog(BasePage):
    DIALOG_TITLE = (AppiumBy.ID, "com.saucelabs.mydemoapp.android:id/alertTitle")
    CONFIRM_BUTTON = (AppiumBy.ID, "android:id/button1")
    CANCEL_BUTTON = (AppiumBy.ID, "android:id/button2")

    def is_displayed(self) -> bool:
        try:
            return self.find(*self.DIALOG_TITLE)
        except Exception:
            return False

    def confirm_logout(self):
        self.click(*self.CONFIRM_BUTTON)

    def cancel_logout(self):
        self.click(*self.CANCEL_BUTTON)
