"""
home_page.py — Page Object for Speechify's main Library/Home screen.

After a user logs in, they land on the Home screen (their document library).
This page object covers all actions available there.
"""

from page_objects.base_page import BasePage


class HomePage(BasePage):
    """Represents the Speechify Library/Home screen after login."""

    # ── Accessibility IDs ─────────────────────────────────────────────────────

    ADD_BUTTON = "addContentButton"
    IMPORT_PDF_OPTION = "importPDFOption"
    IMPORT_GDRIVE_OPTION = "importFromGoogleDriveOption"
    IMPORT_WEB_OPTION = "importFromWebOption"
    LIBRARY_TITLE = "libraryTitleLabel"
    FIRST_DOCUMENT = "documentCell_0"
    SETTINGS_BUTTON = "settingsButton"
    SEARCH_BUTTON = "searchButton"
    SEARCH_FIELD = "searchTextField"
    EMPTY_LIBRARY_LABEL = "emptyLibraryLabel"
    PREMIUM_BANNER = "premiumUpgradeBanner"

    # ── Navigation ────────────────────────────────────────────────────────────

    def tap_add_content(self):
        """Tap the '+' button to add a new document."""
        self.tap(self.ADD_BUTTON)

    def tap_import_pdf(self):
        """Select the 'Import PDF' option from the add-content menu."""
        self.tap_add_content()
        self.tap(self.IMPORT_PDF_OPTION)

    def tap_import_from_google_drive(self):
        """Select 'Import from Google Drive' option."""
        self.tap_add_content()
        self.tap(self.IMPORT_GDRIVE_OPTION)

    def tap_import_from_web(self):
        """Select 'Import from Web URL' option."""
        self.tap_add_content()
        self.tap(self.IMPORT_WEB_OPTION)

    def tap_settings(self):
        """Open the Settings screen."""
        self.tap(self.SETTINGS_BUTTON)

    def tap_first_document(self):
        """Tap the first document in the library to open it."""
        self.tap(self.FIRST_DOCUMENT)

    # ── Search ────────────────────────────────────────────────────────────────

    def search_for_document(self, query: str):
        """Use the search bar to find a document by name."""
        self.tap(self.SEARCH_BUTTON)
        self.type_text(self.SEARCH_FIELD, query)

    # ── State checks ──────────────────────────────────────────────────────────

    def is_home_screen_displayed(self) -> bool:
        """Return True if the library/home screen title is visible."""
        return self.is_element_visible(self.LIBRARY_TITLE)

    def is_library_empty(self) -> bool:
        """Return True if the empty-state message is shown (no documents)."""
        return self.is_element_visible(self.EMPTY_LIBRARY_LABEL, timeout=5)

    def is_premium_banner_shown(self) -> bool:
        """Return True if the premium upsell banner is displayed."""
        return self.is_element_visible(self.PREMIUM_BANNER, timeout=3)
