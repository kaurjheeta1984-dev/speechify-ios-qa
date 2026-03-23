"""
conftest.py — Global pytest fixtures and Appium driver setup.

This file is automatically loaded by pytest before any tests run.
It sets up the Appium driver (the connection to the iOS simulator)
and tears it down cleanly after each test session.
"""

import pytest
import json
import os
from appium import webdriver
from appium.options.ios import XCUITestOptions


# ── Load test config ──────────────────────────────────────────────────────────

def load_config():
    """Read device settings from test_data/test_config.json."""
    config_path = os.path.join(os.path.dirname(__file__), "test_data", "test_config.json")
    with open(config_path, "r") as f:
        return json.load(f)


# ── Appium driver fixture ─────────────────────────────────────────────────────

@pytest.fixture(scope="session")
def driver():
    """
    Session-scoped fixture: starts ONE Appium driver for the whole test run.
    'scope=session' means the app launches once and stays open across all tests
    — faster than restarting for every single test.
    """
    config = load_config()

    options = XCUITestOptions()
    options.platform_name = "iOS"
    options.platform_version = config.get("platformVersion", "17.0")
    options.device_name = config.get("deviceName", "iPhone 15")
    options.app = config.get("appPath", "")           # path to .app or bundle ID
    options.bundle_id = config.get("bundleId", "com.speechify.SpokenLayer")
    options.automation_name = "XCUITest"
    options.no_reset = False                           # fresh app state each session
    options.full_reset = False

    # Connect to local Appium server
    appium_server = config.get("appiumServer", "http://127.0.0.1:4723")

    driver = webdriver.Remote(appium_server, options=options)
    driver.implicitly_wait(10)   # wait up to 10s for elements to appear

    yield driver   # hand the driver to each test

    driver.quit()  # clean up after all tests finish


@pytest.fixture(scope="function")
def reset_app(driver):
    """
    Function-scoped fixture: resets app state before each test that uses it.
    Use this for tests that need a clean slate (e.g., onboarding tests).
    """
    driver.reset()
    yield driver


# ── Reporting helpers ─────────────────────────────────────────────────────────

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    """
    Automatically take a screenshot when a test FAILS.
    The screenshot is attached to the HTML report.
    """
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshot_dir = "reports/screenshots"
            os.makedirs(screenshot_dir, exist_ok=True)
            screenshot_path = os.path.join(screenshot_dir, f"{item.name}.png")
            driver.save_screenshot(screenshot_path)
            print(f"\n📸 Screenshot saved: {screenshot_path}")
