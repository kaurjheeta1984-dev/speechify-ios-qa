"""
base_page.py — Base class for all Page Objects.

What is a Page Object?
  Instead of writing driver.find_element(...) everywhere in every test,
  we create a "Page" class that represents one screen of the app.
  Tests then call page.tap_play() instead of raw driver commands.
  This makes tests easier to read AND easier to maintain.
"""

from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException


class BasePage:
    """
    Every page class inherits from this base.
    It provides shared helpers: find, tap, type text, scroll, wait, etc.
    """

    DEFAULT_TIMEOUT = 10  # seconds to wait for an element

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, self.DEFAULT_TIMEOUT)

    # ── Finding elements ──────────────────────────────────────────────────────

    def find_by_accessibility_id(self, accessibility_id: str):
        """
        Find an element by its Accessibility ID.
        Accessibility IDs are set by developers as labels for screen readers —
        they're the most reliable locator for iOS testing.
        Example: accessibility_id = "playButton"
        """
        return self.wait.until(
            EC.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
        )

    def find_by_xpath(self, xpath: str):
        """Find element by XPath. Use as a fallback when no accessibility ID exists."""
        return self.wait.until(
            EC.presence_of_element_located((AppiumBy.XPATH, xpath))
        )

    def find_by_class_name(self, class_name: str):
        """Find element by iOS class name, e.g. 'XCUIElementTypeButton'."""
        return self.wait.until(
            EC.presence_of_element_located((AppiumBy.CLASS_NAME, class_name))
        )

    # ── Interactions ──────────────────────────────────────────────────────────

    def tap(self, accessibility_id: str):
        """Find an element and tap it."""
        element = self.find_by_accessibility_id(accessibility_id)
        element.click()

    def type_text(self, accessibility_id: str, text: str):
        """Find an input field and type text into it."""
        element = self.find_by_accessibility_id(accessibility_id)
        element.clear()
        element.send_keys(text)

    def get_text(self, accessibility_id: str) -> str:
        """Return the visible text of an element."""
        element = self.find_by_accessibility_id(accessibility_id)
        return element.text

    # ── Visibility checks ─────────────────────────────────────────────────────

    def is_element_visible(self, accessibility_id: str, timeout: int = 5) -> bool:
        """Return True if element appears within timeout, False otherwise."""
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.visibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
            )
            return True
        except TimeoutException:
            return False

    def wait_for_element_to_disappear(self, accessibility_id: str, timeout: int = 10):
        """Wait until a loading spinner or element disappears."""
        WebDriverWait(self.driver, timeout).until(
            EC.invisibility_of_element_located((AppiumBy.ACCESSIBILITY_ID, accessibility_id))
        )

    # ── Scrolling ─────────────────────────────────────────────────────────────

    def scroll_down(self):
        """Swipe up on screen to scroll down (standard iOS gesture)."""
        size = self.driver.get_window_size()
        start_x = size["width"] // 2
        start_y = int(size["height"] * 0.7)
        end_y = int(size["height"] * 0.3)
        self.driver.swipe(start_x, start_y, start_x, end_y, duration=500)

    def scroll_up(self):
        """Swipe down on screen to scroll up."""
        size = self.driver.get_window_size()
        start_x = size["width"] // 2
        start_y = int(size["height"] * 0.3)
        end_y = int(size["height"] * 0.7)
        self.driver.swipe(start_x, start_y, start_x, end_y, duration=500)

    # ── Screenshots ───────────────────────────────────────────────────────────

    def take_screenshot(self, name: str):
        """Save a screenshot to reports/screenshots/."""
        import os
        os.makedirs("reports/screenshots", exist_ok=True)
        path = f"reports/screenshots/{name}.png"
        self.driver.save_screenshot(path)
        return path
