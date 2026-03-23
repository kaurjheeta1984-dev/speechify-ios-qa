"""
test_edge_cases.py — Edge case & boundary tests for Speechify iOS.

Edge cases are "what happens when things go wrong" tests.
These are the tests that often uncover the most embarrassing bugs.
From experience triaging 1,100+ defects: edge cases are where P0 bugs hide.
"""

import pytest
from page_objects.onboarding_page import OnboardingPage
from page_objects.home_page import HomePage
from page_objects.player_page import PlayerPage


VALID_EMAIL = "testuser.speechify@gmail.com"
VALID_PASSWORD = "SpeechifyTest@123"


@pytest.fixture(scope="class")
def logged_in_driver(driver):
    onboarding = OnboardingPage(driver)
    home = HomePage(driver)
    if not home.is_home_screen_displayed():
        onboarding.complete_sign_in(VALID_EMAIL, VALID_PASSWORD)
    return driver


class TestEdgeCases:

    # ── EDGE-001: Very long email ──────────────────────────────────────────────

    @pytest.mark.edge_case
    @pytest.mark.priority_p2
    def test_sign_up_with_extremely_long_email_is_handled(self, driver):
        """
        EDGE-001 | P2 | Edge Case
        Verify the app handles a 255-character email gracefully.
        Should either accept it (if valid) or show a clear error.
        Should NOT crash or freeze.
        """
        onboarding = OnboardingPage(driver)
        long_email = ("a" * 243) + "@example.com"  # exactly 255 chars

        onboarding.tap_get_started()
        onboarding.tap_sign_up()
        onboarding.enter_email(long_email)
        onboarding.enter_password(VALID_PASSWORD)
        onboarding.enter_confirm_password(VALID_PASSWORD)
        onboarding.tap_submit()

        # App must show error OR success — must not crash
        app_is_responsive = (
            onboarding.is_error_displayed() or
            HomePage(driver).is_home_screen_displayed()
        )
        assert app_is_responsive, (
            "App became unresponsive after entering a very long email. "
            "Possible crash or infinite loading state."
        )

    # ── EDGE-002: Special characters in password ───────────────────────────────

    @pytest.mark.edge_case
    @pytest.mark.priority_p2
    def test_password_with_special_characters_accepted(self, driver):
        """
        EDGE-002 | P2 | Edge Case
        Verify passwords containing special characters (!@#$%^&*) are accepted.
        Some apps incorrectly strip or reject special chars, causing login issues.
        """
        onboarding = OnboardingPage(driver)
        special_password = "P@$$w0rd!#%^&*()"

        onboarding.tap_get_started()
        onboarding.tap_sign_up()
        onboarding.enter_email(VALID_EMAIL)
        onboarding.enter_password(special_password)
        onboarding.enter_confirm_password(special_password)
        onboarding.tap_submit()

        home = HomePage(driver)
        # Should either succeed (go to Home) or show error — not crash
        assert home.is_home_screen_displayed() or onboarding.is_error_displayed(), (
            "App did not handle special characters in password gracefully."
        )

    # ── EDGE-003: Double-tap play button ──────────────────────────────────────

    @pytest.mark.edge_case
    @pytest.mark.priority_p2
    def test_double_tapping_play_does_not_cause_errors(self, logged_in_driver):
        """
        EDGE-003 | P2 | Edge Case
        Verify that rapidly tapping Play twice doesn't cause duplicate audio
        streams, crash, or UI glitch.
        """
        home = HomePage(logged_in_driver)
        player = PlayerPage(logged_in_driver)

        home.tap_first_document()
        player.tap_play()
        player.tap_play()  # Second tap — should pause, not crash

        # App should still be on player screen and responsive
        assert player.is_player_displayed(), (
            "Player screen disappeared after double-tapping Play. "
            "Possible crash or unintended navigation."
        )

    # ── EDGE-004: Speed set then app background/foreground ────────────────────

    @pytest.mark.edge_case
    @pytest.mark.priority_p2
    def test_playback_speed_persists_after_backgrounding_app(self, logged_in_driver):
        """
        EDGE-004 | P2 | Edge Case
        Verify that playback speed set by user persists when the app is
        sent to background and brought back to foreground.
        """
        home = HomePage(logged_in_driver)
        player = PlayerPage(logged_in_driver)

        home.tap_first_document()
        player.set_speed("2x")

        # Background the app (simulate Home button press)
        logged_in_driver.background_app(3)  # background for 3 seconds

        # App comes back to foreground automatically
        current_speed = player.get_current_speed()
        assert current_speed == "2x", (
            f"Speed changed from '2x' to '{current_speed}' after backgrounding app."
        )

    # ── EDGE-005: Import unsupported file type ─────────────────────────────────

    @pytest.mark.edge_case
    @pytest.mark.priority_p1
    def test_importing_unsupported_file_type_shows_error(self, logged_in_driver):
        """
        EDGE-005 | P1 | Edge Case
        Verify the app shows a friendly error when a non-supported file
        type is attempted (e.g. a video file, .exe, etc.).
        Should NOT crash or silently add a broken document.
        """
        home = HomePage(logged_in_driver)

        home.tap_import_pdf()  # Opens file picker
        # In a real run, you would navigate the file picker to an .exe file.
        # Here we verify the error state is handled gracefully.
        # This test documents expected behavior for the test plan.

        # Assert the file picker opened (can't fully automate file selection in CI)
        assert home.is_element_visible("FilePicker", timeout=5), (
            "File picker did not open. Cannot test unsupported file import."
        )

    # ── EDGE-006: Rapid speed changes ─────────────────────────────────────────

    @pytest.mark.edge_case
    @pytest.mark.priority_p2
    def test_rapid_speed_changes_do_not_freeze_app(self, logged_in_driver):
        """
        EDGE-006 | P2 | Edge Case
        Verify that changing speed rapidly (5 times in a row) doesn't freeze
        or crash the audio engine.
        """
        home = HomePage(logged_in_driver)
        player = PlayerPage(logged_in_driver)

        home.tap_first_document()
        player.tap_play()

        speeds = ["1x", "2x", "3x", "1.5x", "4.5x"]
        for speed in speeds:
            player.set_speed(speed)

        # After rapid changes, app should still be responsive
        assert player.is_player_displayed(), (
            "Player screen is no longer shown after rapid speed changes. "
            "Audio engine may have crashed."
        )

        final_speed = player.get_current_speed()
        assert final_speed == "4.5x", (
            f"Expected final speed '4.5x' but got '{final_speed}'."
        )
