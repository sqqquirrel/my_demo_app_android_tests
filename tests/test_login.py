import allure
import pytest

from pages.components.logout_dialog import LogoutDialog
from pages.components.menu_element import MenuElement
from pages.login_page import LoginPage
from test_data.user_data import VALID_USER, INVALID_USER


def login_user(driver, login, password):
    menu = MenuElement(driver)
    with allure.step("Click login in menu"):
        menu.open_menu()
        menu.click_login()
    login_page = LoginPage(driver)
    with allure.step(f"Login with username='{login}'"):
        login_page.login(login, password)


@allure.feature('Login')
class TestLogin:

    @allure.title("Valid login should show logout button")
    def test_valid_login_logout(self, driver, auto_logout):
        login_user(driver, VALID_USER["username"], VALID_USER["password"])

        menu = MenuElement(driver)
        with allure.step("Open menu and check logout button"):
            menu.open_menu()
            assert menu.is_logout_button_visible(), "Logout button not appeared after login"

    @pytest.mark.xfail(
        reason="BUG: App accepts any password for login. Should reject invalid credentials.",
        strict=True
    )
    @allure.title("Invalid login should show error message and login button")
    def test_invalid_login(self, driver, auto_logout):
        login_user(driver, INVALID_USER["username"], INVALID_USER["password"])
        login_page = LoginPage(driver)

        with allure.step("Check error message is displayed"):
            error_text = login_page.get_error_message()
            assert error_text is not None, "Error message not shown"
            assert "Username and password do not match" in error_text or "invalid" in error_text.lower(), \
                f"Incorrect error message: {error_text}"

        menu = MenuElement(driver)
        with allure.step("Check login button is visible after failed login"):
            menu.open_menu()
            assert menu.is_login_button_visible(), "Login button not appeared after unsuccessful login"

    @allure.title("Logout should hide logout button and show login button")
    def test_logout(self, driver, auto_logout):
        login_user(driver, VALID_USER["username"], VALID_USER["password"])

        menu = MenuElement(driver)
        with allure.step("Open menu and logout if possible"):
            menu.open_menu()
            if menu.is_logout_button_visible():
                menu.click_logout()

        with allure.step("Confirm logout dialog"):
            logout_dialog = LogoutDialog(driver)
            logout_dialog.confirm_logout()

        with allure.step("Check login page and login button are visible after logout"):
            LoginPage(driver)
            menu.open_menu()
            assert menu.is_login_button_visible(), "Login button not appeared after logout"


@pytest.fixture
def auto_logout(driver):
    yield
    menu = MenuElement(driver)
    menu.open_menu()
    try:
        if menu.is_logout_button_visible():
            menu.click_logout()
            dialog = LogoutDialog(driver)
            if dialog.is_displayed():
                dialog.confirm_logout()
    except Exception:
        pass
