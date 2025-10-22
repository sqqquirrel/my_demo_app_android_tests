import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from appium.webdriver.common.appiumby import AppiumBy


class BasePage:
    """Base class for all pages and UI components."""

    def __init__(self, driver):
        self.driver = driver

        self.timeout = 10
        self.wait = WebDriverWait(driver, self.timeout)

    # ---------- Core Find & Click ----------

    @allure.step("Find element: {locator}")
    def find(self, by, locator, timeout=None):
        """Wait for element to be visible and return it."""
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.presence_of_element_located((by, locator))
        )

    def find_all(self, by, locator, timeout=None):
        """Find all elements (no exception if empty)."""
        try:
            wait = WebDriverWait(self.driver, timeout or self.timeout)
            return wait.until(EC.presence_of_all_elements_located((by, locator)))
        except TimeoutException:
            return []

    @allure.step("Click element: {locator}")
    def click(self, by, locator, timeout=None):
        """Click element when clickable."""
        element = self.find(by, locator, timeout)
        element.click()

    def get_text(self, by, locator, timeout=None) -> str:
        """Get visible text of element."""
        element = self.find(by, locator, timeout)
        return element.text.strip()

    def send_keys(self, by, locator, text, timeout=None):
        element = self.find(by, locator, timeout)
        element.clear()
        element.send_keys(text)

    # ---------- Waits & Conditions ----------

    def is_element_visible(self, locator, timeout=5) -> bool:
        """Check if element becomes visible within timeout."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))
            return True
        except TimeoutException:
            return False

    def is_element_clickable(self, locator, timeout=5) -> bool:
        """Check if element becomes clickable."""
        try:
            WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))
            return True
        except TimeoutException:
            return False

    # ---------- Utility ----------
    def is_page_displayed(self, title_text: str, timeout=5) -> bool:
        """Generic check that a page with certain header text is displayed."""
        xpath = f"//android.widget.TextView[@text='{title_text}']"
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((AppiumBy.XPATH, xpath))
            )
            return True
        except TimeoutException:
            return False
