"""
player_page.py — Page Object for Speechify's Audio Player screen.

When a user opens a document, the Player screen loads.
This page object handles all playback controls and settings.
"""

from page_objects.base_page import BasePage


class PlayerPage(BasePage):
    """Represents the Speechify Audio Player screen."""

    # ── Accessibility IDs ─────────────────────────────────────────────────────

    PLAY_BUTTON = "playButton"
    PAUSE_BUTTON = "pauseButton"
    REWIND_BUTTON = "rewindButton"
    FORWARD_BUTTON = "forwardButton"
    SPEED_CONTROL = "speedControlButton"
    SPEED_LABEL = "currentSpeedLabel"
    VOICE_SELECTOR = "voiceSelectorButton"
    FONT_SIZE_INCREASE = "fontSizeIncreaseButton"
    FONT_SIZE_DECREASE = "fontSizeDecreaseButton"
    PROGRESS_BAR = "playbackProgressBar"
    CURRENT_TIME_LABEL = "currentTimeLabel"
    TOTAL_TIME_LABEL = "totalTimeLabel"
    DOCUMENT_TITLE_LABEL = "documentTitleLabel"
    CLOSE_PLAYER_BUTTON = "closePlayerButton"
    BOOKMARK_BUTTON = "bookmarkButton"
    SHARE_BUTTON = "shareButton"

    # ── Playback controls ─────────────────────────────────────────────────────

    def tap_play(self):
        """Tap Play to start audio playback."""
        self.tap(self.PLAY_BUTTON)

    def tap_pause(self):
        """Tap Pause to stop audio playback."""
        self.tap(self.PAUSE_BUTTON)

    def tap_rewind(self):
        """Tap the rewind button (go back in audio)."""
        self.tap(self.REWIND_BUTTON)

    def tap_forward(self):
        """Tap the forward button (skip ahead in audio)."""
        self.tap(self.FORWARD_BUTTON)

    def tap_close(self):
        """Close the player and return to the library."""
        self.tap(self.CLOSE_PLAYER_BUTTON)

    # ── Speed controls ────────────────────────────────────────────────────────

    def tap_speed_control(self):
        """Open the speed selector panel."""
        self.tap(self.SPEED_CONTROL)

    def get_current_speed(self) -> str:
        """Return the currently displayed playback speed (e.g. '1.5x')."""
        return self.get_text(self.SPEED_LABEL)

    def set_speed(self, speed_value: str):
        """
        Set playback speed by tapping the speed control and selecting a value.
        speed_value examples: '0.5x', '1x', '1.5x', '2x', '3x', '4.5x'
        """
        self.tap_speed_control()
        # Speed options appear as accessibility IDs like "speed_1.5x"
        speed_id = f"speed_{speed_value}"
        self.tap(speed_id)

    # ── Voice controls ────────────────────────────────────────────────────────

    def tap_voice_selector(self):
        """Open the voice selection panel."""
        self.tap(self.VOICE_SELECTOR)

    # ── State checks ──────────────────────────────────────────────────────────

    def is_player_displayed(self) -> bool:
        """Return True if the audio player screen is visible."""
        return self.is_element_visible(self.PLAY_BUTTON)

    def is_playing(self) -> bool:
        """
        Return True if audio is currently playing.
        When playing, the Pause button is visible; Play button is hidden.
        """
        return self.is_element_visible(self.PAUSE_BUTTON, timeout=3)

    def is_paused(self) -> bool:
        """Return True if playback is currently paused."""
        return self.is_element_visible(self.PLAY_BUTTON, timeout=3)

    def get_document_title(self) -> str:
        """Return the title of the currently open document."""
        return self.get_text(self.DOCUMENT_TITLE_LABEL)

    def get_current_time(self) -> str:
        """Return the current playback time (e.g. '0:42')."""
        return self.get_text(self.CURRENT_TIME_LABEL)

    def get_total_time(self) -> str:
        """Return the total document length (e.g. '12:30')."""
        return self.get_text(self.TOTAL_TIME_LABEL)
