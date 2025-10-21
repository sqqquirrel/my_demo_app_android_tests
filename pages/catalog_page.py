from appium.webdriver.common.appiumby import AppiumBy
from pages.base_page import BasePage
from pages.components.menu_element import MenuElement


class CatalogPage(BasePage):
    PAGE_TITLE = "Products"

    PRODUCT_CONTAINER = (
        AppiumBy.XPATH,
        "//android.view.ViewGroup[.//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/titleTV']]",
    )
    PRODUCT_PRICE = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/priceTV",
    )
    PRODUCT_IMAGE = (
        AppiumBy.ID,
        "com.saucelabs.mydemoapp.android:id/productIV",
    )

    SORTING_BUTTON = (
        AppiumBy.ACCESSIBILITY_ID,
        "Shows current sorting order and displays available sorting options",
    )
    SORT_BY_NAME_ASC = (
        AppiumBy.ACCESSIBILITY_ID,
        "Displays ascending sorting order by name",
    )
    SORT_BY_NAME_DESC = (
        AppiumBy.ACCESSIBILITY_ID,
        "Displays descending sorting order by name",
    )
    SORT_BY_PRICE_ASC = (
        AppiumBy.ACCESSIBILITY_ID,
        "Displays ascending sorting order by price",
    )
    SORT_BY_PRICE_DESC = (
        AppiumBy.ACCESSIBILITY_ID,
        "Displays descending sorting order by price",
    )

    def __init__(self, driver):
        super().__init__(driver)
        self.menu = MenuElement(driver)
        assert self.is_page_displayed(self.PAGE_TITLE), f"{self.PAGE_TITLE} page is not displayed"

    def _build_product_container_xpath(self, name: str) -> str:
        return (
            f"//android.view.ViewGroup[.//android.widget.TextView"
            f"[@resource-id='com.saucelabs.mydemoapp.android:id/titleTV' and @text='{name}']]"
        )

    def open_product_by_name(self, name: str):
        container_xpath = self._build_product_container_xpath(name)
        image_xpath = f"{container_xpath}//android.widget.ImageView[@resource-id='com.saucelabs.mydemoapp.android:id/productIV']"
        self.find(AppiumBy.XPATH, image_xpath).click()

    def get_price_by_name(self, name: str) -> str:
        container_xpath = self._build_product_container_xpath(name)
        price_xpath = f"{container_xpath}//android.widget.TextView[@resource-id='com.saucelabs.mydemoapp.android:id/priceTV']"
        return self.find(AppiumBy.XPATH, price_xpath).text

    def get_all_prices(self) -> list[str]:
        elements = self.driver.find_elements(*self.PRODUCT_PRICE)
        return [el.text for el in elements]

    def is_product_displayed(self, name: str) -> bool:
        try:
            self.find(AppiumBy.XPATH, self._build_product_container_xpath(name))
            return True
        except Exception:
            return False

    def open_sorting_menu(self):
        self.click(*self.SORTING_BUTTON)

    def sort_by_price_asc(self):
        self.open_sorting_menu()
        self.click(*self.SORT_BY_PRICE_ASC)

    def sort_by_price_desc(self):
        self.open_sorting_menu()
        self.click(*self.SORT_BY_PRICE_DESC)

    def sort_by_name_asc(self):
        self.open_sorting_menu()
        self.click(*self.SORT_BY_NAME_ASC)

    def sort_by_name_desc(self):
        self.open_sorting_menu()
        self.click(*self.SORT_BY_NAME_DESC)
