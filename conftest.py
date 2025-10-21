import allure
from appium import webdriver
import os
import pytest
from appium.options.android import UiAutomator2Options
from selenium.common import WebDriverException


@pytest.fixture(scope='session')
def driver():
    appium_server = os.environ.get("APPIUM_SERVER", "http://127.0.0.1:4723")
    app_path = os.environ.get("APP_PATH", "app/mda-2.2.0-25.apk")

    options = UiAutomator2Options()
    options.platform_name = "Android"
    options.device_name = "emulator-5554"
    options.app = app_path
    options.automation_name = "UiAutomator2"
    options.auto_grant_permissions = True

    try:
        driver = webdriver.Remote(command_executor=appium_server, options=options)
    except WebDriverException as e:
        raise RuntimeError(f"Could not connect to Appium server at {appium_server}") from e
    yield driver
    driver.quit()


# Attach screenshot on failure
@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    rep = outcome.get_result()
    if rep.when == 'call' and rep.failed:
        driver_fixture = item.funcargs.get('driver')
        if driver_fixture:
            try:
                png = driver_fixture.get_screenshot_as_png()
                allure.attach(png, name=f"screenshot-{item.name}", attachment_type=allure.attachment_type.PNG)
            except Exception:
                pass
