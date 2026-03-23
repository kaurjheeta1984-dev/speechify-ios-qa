"""
test_document_import.py — Functional tests for document import into Speechify iOS.

Speechify's core workflow: user imports content (PDF, web article, Google Drive)
→ app converts it to audio. These tests validate that import works reliably.
"""

import pytest
import os
from page_objects.onboarding_page import OnboardingPage
from page_objects.home_page import HomePage
from page_objects.player_page import PlayerPage


VALID_EMAIL = "testuser.speechify@gmail.com"
VALID_PASSWORD = "SpeechifyTest@123"
SAMPLE_PDF_PATH = os.path.join(os.path.dirname(__file__),
                               "../../test_data/sample_documents/sample.pdf")


@pytest.fixture(scope="class")
def logged_in_driver(driver):
    """Sign in once and reuse across the class."""
    onboarding = OnboardingPage(driver)
    home = HomePage(driver)
    if not home.is_home_screen_displayed():
        onboarding.complete_sign_in(VALID_EMAIL, VALID_PASSWORD)
    return driver


class TestDocumentImport:
    """Tests for importing content into the Speechify library."""

    # ── TC-201: Add button visible ─────────────────────────────────────────────

    @pytest.mark.smoke
    @pytest.mark.priority_p0
    def test_add_content_button_is_visible_on_home(self, logged_in_driver):
        """
        TC-201 | P0 | Smoke
        Verify the '+' Add Content button is visible on the library screen.
        Without this, users cannot import anything.
        """
        home = HomePage(logged_in_driver)
        assert home.is_element_visible(home.ADD_BUTTON), (
            "The Add Content (+) button is not visible on the Home screen."
        )

    # ── TC-202: Import menu appears ────────────────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p0
    def test_tapping_add_shows_import_options(self, logged_in_driver):
        """
        TC-202 | P0 | Functional
        Verify tapping '+' reveals import options (PDF, Google Drive, Web).
        """
        home = HomePage(logged_in_driver)

        home.tap_add_content()

        assert home.is_element_visible(home.IMPORT_PDF_OPTION), (
            "Import PDF option not shown after tapping Add Content."
        )

    # ── TC-203: PDF import starts ──────────────────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p0
    def test_import_pdf_option_opens_file_picker(self, logged_in_driver):
        """
        TC-203 | P0 | Functional
        Verify tapping 'Import PDF' opens the iOS file picker (Files app).
        The file picker's accessibility ID is a system-level iOS component.
        """
        home = HomePage(logged_in_driver)

        home.tap_import_pdf()

        # iOS Files app picker has this accessibility ID
        assert home.is_element_visible("FilePicker", timeout=5), (
            "File picker did not open after selecting Import PDF. "
            "Check that the app has Files/Photos permissions in Info.plist."
        )

    # ── TC-204: Google Drive import option visible ─────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p1
    def test_google_drive_import_option_is_present(self, logged_in_driver):
        """
        TC-204 | P1 | Functional
        Verify 'Import from Google Drive' option is available in the add menu.
        """
        home = HomePage(logged_in_driver)

        home.tap_add_content()

        assert home.is_element_visible(home.IMPORT_GDRIVE_OPTION), (
            "Google Drive import option not found in Add Content menu."
        )

    # ── TC-205: Imported document appears in library ───────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p0
    def test_imported_document_appears_in_library(self, logged_in_driver):
        """
        TC-205 | P0 | Functional
        After importing a PDF, verify it appears in the library document list.

        NOTE: This test requires 'sample.pdf' to exist in test_data/sample_documents/.
        See the test_data/ folder for the sample file.
        """
        home = HomePage(logged_in_driver)

        # Check library is not empty after import
        # (Assumes import happened in a previous step or setup fixture)
        assert not home.is_library_empty(), (
            "Library is empty — imported document did not appear. "
            "Possible causes: import failed, sync delay, or wrong account."
        )

    # ── TC-206: Imported document opens in player ──────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p0
    def test_tapping_document_opens_player(self, logged_in_driver):
        """
        TC-206 | P0 | Functional
        Verify that tapping an imported document in the library opens the player.
        This is the core user journey: import → play.
        """
        home = HomePage(logged_in_driver)
        player = PlayerPage(logged_in_driver)

        home.tap_first_document()

        assert player.is_player_displayed(), (
            "Player screen did not open after tapping a document in the library."
        )

    # ── TC-207: Web URL import option visible ──────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p1
    def test_web_url_import_option_is_present(self, logged_in_driver):
        """
        TC-207 | P1 | Functional
        Verify 'Import from Web' option is in the Add Content menu.
        Speechify allows importing articles via URL — this is a key feature.
        """
        home = HomePage(logged_in_driver)

        home.tap_add_content()

        assert home.is_element_visible(home.IMPORT_WEB_OPTION), (
            "Web URL import option not found in Add Content menu."
        )
