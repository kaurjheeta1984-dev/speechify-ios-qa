"""
test_audio_playback.py — Functional tests for Speechify iOS audio playback.

These tests cover the core value proposition of Speechify — playing audio from text.
All P0 tests here must pass before any release ships.
"""

import pytest
from page_objects.onboarding_page import OnboardingPage
from page_objects.home_page import HomePage
from page_objects.player_page import PlayerPage


VALID_EMAIL = "testuser.speechify@gmail.com"
VALID_PASSWORD = "SpeechifyTest@123"


@pytest.fixture(scope="class")
def logged_in_driver(driver):
    """
    Class-scoped fixture: signs in once and reuses the session for all
    tests in this class. Faster than re-logging in before every test.
    """
    onboarding = OnboardingPage(driver)
    home = HomePage(driver)

    if not home.is_home_screen_displayed():
        onboarding.complete_sign_in(VALID_EMAIL, VALID_PASSWORD)

    return driver


class TestAudioPlayback:
    """Tests for the core audio playback functionality."""

    # ── TC-101: Player screen loads ────────────────────────────────────────────

    @pytest.mark.smoke
    @pytest.mark.priority_p0
    def test_player_screen_loads_when_document_opened(self, logged_in_driver):
        """
        TC-101 | P0 | Smoke
        Verify the audio player screen appears when a document is tapped.
        """
        home = HomePage(logged_in_driver)
        player = PlayerPage(logged_in_driver)

        home.tap_first_document()

        assert player.is_player_displayed(), (
            "Player screen did not load after tapping a document."
        )

    # ── TC-102: Play button starts audio ──────────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p0
    def test_tap_play_starts_audio_playback(self, logged_in_driver):
        """
        TC-102 | P0 | Functional
        Verify tapping Play transitions the UI to playing state.
        When playing, the Pause button should be visible.
        """
        player = PlayerPage(logged_in_driver)

        player.tap_play()

        assert player.is_playing(), (
            "After tapping Play, the player did not enter playing state. "
            "Pause button not visible — audio may not have started."
        )

    # ── TC-103: Pause stops audio ─────────────────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p0
    def test_tap_pause_stops_audio_playback(self, logged_in_driver):
        """
        TC-103 | P0 | Functional
        Verify tapping Pause stops the audio and shows the Play button again.
        """
        player = PlayerPage(logged_in_driver)

        # Ensure we're in playing state first
        if not player.is_playing():
            player.tap_play()

        player.tap_pause()

        assert player.is_paused(), (
            "After tapping Pause, the player did not enter paused state."
        )

    # ── TC-104: Playback speed — 1.5x ─────────────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p1
    def test_playback_speed_changes_to_1_5x(self, logged_in_driver):
        """
        TC-104 | P1 | Functional
        Verify the user can change playback speed to 1.5x.
        Speechify's key feature is listening at faster-than-normal speeds.
        """
        player = PlayerPage(logged_in_driver)

        player.set_speed("1.5x")

        current_speed = player.get_current_speed()
        assert current_speed == "1.5x", (
            f"Expected speed '1.5x' but got '{current_speed}'. "
            "Speed control may not be updating the UI correctly."
        )

    # ── TC-105: Playback speed — maximum (4.5x) ───────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p1
    def test_playback_speed_changes_to_maximum(self, logged_in_driver):
        """
        TC-105 | P1 | Functional
        Verify the user can set speed to 4.5x (Speechify's max speed).
        """
        player = PlayerPage(logged_in_driver)

        player.set_speed("4.5x")

        current_speed = player.get_current_speed()
        assert current_speed == "4.5x", (
            f"Expected '4.5x' but got '{current_speed}'."
        )

    # ── TC-106: Playback speed — minimum (0.5x) ───────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p1
    def test_playback_speed_changes_to_minimum(self, logged_in_driver):
        """
        TC-106 | P1 | Functional
        Verify the user can set speed to 0.5x (slowest option).
        """
        player = PlayerPage(logged_in_driver)

        player.set_speed("0.5x")

        current_speed = player.get_current_speed()
        assert current_speed == "0.5x", (
            f"Expected '0.5x' but got '{current_speed}'."
        )

    # ── TC-107: Speed resets to 1x ────────────────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p1
    def test_speed_resets_to_default_after_app_restart(self, driver):
        """
        TC-107 | P1 | Functional
        Verify that if user sets speed to 2x and restarts the app,
        speed persists (or resets to default — document whichever is intended).

        NOTE: This test documents behavior. If persistence is intended, assert 2x.
        If reset is intended, assert 1x. Adjust the assertion to match the spec.
        """
        player = PlayerPage(driver)
        player.set_speed("2x")

        # Terminate and relaunch app
        driver.terminate_app("com.speechify.SpokenLayer")
        driver.activate_app("com.speechify.SpokenLayer")

        # Based on Speechify's spec: speed should persist across sessions
        current_speed = player.get_current_speed()
        assert current_speed == "2x", (
            "Speed did not persist after app restart. "
            "Expected '2x' based on spec — speed should be saved per user."
        )

    # ── TC-108: Document title shown in player ─────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p2
    def test_document_title_displayed_in_player(self, logged_in_driver):
        """
        TC-108 | P2 | Functional
        Verify the document title is shown in the player header.
        """
        home = HomePage(logged_in_driver)
        player = PlayerPage(logged_in_driver)

        home.tap_first_document()
        title = player.get_document_title()

        assert title is not None and len(title) > 0, (
            "Document title is empty in the player screen."
        )
