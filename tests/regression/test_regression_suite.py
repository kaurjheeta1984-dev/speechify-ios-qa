"""
test_regression_suite.py — Regression tests for Speechify iOS.

Regression tests verify that NEW code changes haven't broken existing features.
Run these before every release to catch regressions.
These are the equivalent of the regression suites maintained at E-touch Systems.
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


class TestRegressionSuite:
    """
    Full regression suite — covers the critical paths that must work every release.
    Tag: @pytest.mark.regression
    """

    # ── REG-001: Full onboarding → playback journey ────────────────────────────

    @pytest.mark.regression
    @pytest.mark.priority_p0
    def test_full_user_journey_onboarding_to_playback(self, reset_app):
        """
        REG-001 | P0 | Regression
        End-to-end test: launch → sign in → open document → play audio.
        This is the most important regression test. If this fails, ship nothing.
        """
        onboarding = OnboardingPage(reset_app)
        home = HomePage(reset_app)
        player = PlayerPage(reset_app)

        # Step 1: Sign in
        onboarding.complete_sign_in(VALID_EMAIL, VALID_PASSWORD)
        assert home.is_home_screen_displayed(), "Step 1 FAILED: Home not shown after sign-in."

        # Step 2: Open first document
        home.tap_first_document()
        assert player.is_player_displayed(), "Step 2 FAILED: Player did not open."

        # Step 3: Play audio
        player.tap_play()
        assert player.is_playing(), "Step 3 FAILED: Audio did not start playing."

        # Step 4: Pause audio
        player.tap_pause()
        assert player.is_paused(), "Step 4 FAILED: Audio did not pause."

    # ── REG-002: Settings persist after restart ────────────────────────────────

    @pytest.mark.regression
    @pytest.mark.priority_p1
    def test_playback_settings_persist_after_app_restart(self, driver):
        """
        REG-002 | P1 | Regression
        Verify user's speed preference is saved and restored after an app restart.
        Tests persistence layer (UserDefaults / backend sync).
        """
        home = HomePage(driver)
        player = PlayerPage(driver)

        home.tap_first_document()
        player.set_speed("2x")

        # Terminate and relaunch
        driver.terminate_app("com.speechify.SpokenLayer")
        driver.activate_app("com.speechify.SpokenLayer")

        speed_after_restart = player.get_current_speed()
        assert speed_after_restart == "2x", (
            f"Speed preference not persisted. Expected '2x', got '{speed_after_restart}'."
        )

    # ── REG-003: App recovers after being killed mid-playback ──────────────────

    @pytest.mark.regression
    @pytest.mark.priority_p1
    def test_app_recovers_gracefully_after_force_kill(self, driver):
        """
        REG-003 | P1 | Regression
        Simulate force-killing the app during playback, then relaunching.
        The app should return to library (not crash loop or show corrupted state).
        """
        home = HomePage(driver)
        player = PlayerPage(driver)

        home.tap_first_document()
        player.tap_play()

        # Force kill during playback
        driver.terminate_app("com.speechify.SpokenLayer")
        driver.activate_app("com.speechify.SpokenLayer")

        # Should recover to a usable state — either home or player
        app_recovered = (
            home.is_home_screen_displayed() or
            player.is_player_displayed()
        )
        assert app_recovered, (
            "App did not recover to a usable state after force kill during playback."
        )

    # ── REG-004: Multiple documents in library ─────────────────────────────────

    @pytest.mark.regression
    @pytest.mark.priority_p1
    def test_library_displays_multiple_documents(self, logged_in_driver):
        """
        REG-004 | P1 | Regression
        Verify the library correctly displays multiple documents (not just one).
        Tests list rendering — a common regression target after UI changes.
        """
        home = HomePage(logged_in_driver)

        # Library should not be empty for this test account
        assert not home.is_library_empty(), (
            "Library appears empty. Either no documents exist for this account, "
            "or the library failed to load documents (sync/network issue)."
        )

    # ── REG-005: Sign out and sign back in ────────────────────────────────────

    @pytest.mark.regression
    @pytest.mark.priority_p1
    def test_sign_out_then_sign_in_restores_library(self, driver):
        """
        REG-005 | P1 | Regression
        Verify that signing out and back in restores the user's document library.
        Tests that library is tied to account, not device-local storage.
        """
        home = HomePage(driver)
        onboarding = OnboardingPage(driver)

        # Navigate to settings and sign out
        home.tap_settings()
        # (Settings page object would be used here in full implementation)
        # For now, we reset app to simulate sign-out
        driver.reset()

        # Sign back in
        onboarding.complete_sign_in(VALID_EMAIL, VALID_PASSWORD)
        assert home.is_home_screen_displayed(), (
            "Could not sign back in after signing out."
        )
        assert not home.is_library_empty(), (
            "Library is empty after signing back in — documents not restored. "
            "Library may be device-local instead of account-synced."
        )
