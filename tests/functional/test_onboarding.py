"""
test_onboarding.py — Functional tests for Speechify iOS onboarding & authentication.

Test IDs map to the test plan in docs/TEST_PLAN.md.
Priority levels follow the same P0/P1/P2 system used at E-touch Systems (Google).
  P0 = app-breaking, must pass before any release
  P1 = important feature, blocks release if failing
  P2 = nice-to-have, can ship with known issue + ticket
"""

import pytest
from page_objects.onboarding_page import OnboardingPage
from page_objects.home_page import HomePage


# ── Test data ──────────────────────────────────────────────────────────────────

VALID_EMAIL = "testuser.speechify@gmail.com"
VALID_PASSWORD = "SpeechifyTest@123"
INVALID_EMAIL = "not-an-email"
WRONG_PASSWORD = "wrongpassword"
EMPTY_STRING = ""


# ── Test class ─────────────────────────────────────────────────────────────────

class TestOnboarding:
    """
    All tests in this class test the onboarding & authentication flow.
    Each test method starts with 'test_' so pytest discovers it automatically.
    """

    # ── TC-001: App launch ─────────────────────────────────────────────────────

    @pytest.mark.smoke
    @pytest.mark.priority_p0
    def test_app_launches_and_shows_welcome_screen(self, driver):
        """
        TC-001 | P0 | Smoke
        Verify the app launches successfully and the welcome screen is shown.
        This is the most basic test — if this fails, nothing else will work.
        """
        onboarding = OnboardingPage(driver)

        assert onboarding.is_welcome_screen_displayed(), (
            "Welcome screen was NOT displayed after app launch. "
            "Possible causes: app crash on startup, white screen, or wrong bundle ID."
        )

    # ── TC-002: Valid sign-up ──────────────────────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p0
    def test_sign_up_with_valid_credentials(self, reset_app):
        """
        TC-002 | P0 | Functional
        Verify a new user can successfully sign up with valid email + password.
        After sign-up, the user should be on the Home/Library screen.
        """
        onboarding = OnboardingPage(reset_app)
        home = HomePage(reset_app)

        onboarding.complete_sign_up(VALID_EMAIL, VALID_PASSWORD)

        assert home.is_home_screen_displayed(), (
            "After valid sign-up, Home screen was NOT shown. "
            "Sign-up may have failed silently or navigation is broken."
        )

    # ── TC-003: Invalid email format ───────────────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p1
    def test_sign_up_with_invalid_email_shows_error(self, reset_app):
        """
        TC-003 | P1 | Functional
        Verify that entering a malformed email shows a validation error.
        The app should NOT navigate away — it should stay on sign-up and show
        an inline error like 'Please enter a valid email address'.
        """
        onboarding = OnboardingPage(reset_app)

        onboarding.tap_get_started()
        onboarding.tap_sign_up()
        onboarding.enter_email(INVALID_EMAIL)
        onboarding.enter_password(VALID_PASSWORD)
        onboarding.enter_confirm_password(VALID_PASSWORD)
        onboarding.tap_submit()

        assert onboarding.is_error_displayed(), (
            "No error message was shown after submitting an invalid email. "
            "The app should validate email format before allowing submission."
        )

    # ── TC-004: Empty email field ──────────────────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p1
    def test_sign_up_with_empty_email_shows_error(self, reset_app):
        """
        TC-004 | P1 | Functional
        Verify the app blocks submission when email field is blank.
        """
        onboarding = OnboardingPage(reset_app)

        onboarding.tap_get_started()
        onboarding.tap_sign_up()
        onboarding.enter_email(EMPTY_STRING)
        onboarding.enter_password(VALID_PASSWORD)
        onboarding.enter_confirm_password(VALID_PASSWORD)
        onboarding.tap_submit()

        assert onboarding.is_error_displayed(), (
            "Submitting with empty email should show an error, but none appeared."
        )

    # ── TC-005: Wrong password on sign-in ──────────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p1
    def test_sign_in_with_wrong_password_shows_error(self, reset_app):
        """
        TC-005 | P1 | Functional
        Verify the app shows an error when a user signs in with a wrong password.
        It should NOT navigate to the Home screen.
        """
        onboarding = OnboardingPage(reset_app)

        onboarding.complete_sign_in(VALID_EMAIL, WRONG_PASSWORD)

        assert onboarding.is_error_displayed(), (
            "No error shown for incorrect password. "
            "This is a security issue — invalid credentials must be rejected."
        )

    # ── TC-006: Sign-in with valid credentials ─────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p0
    def test_sign_in_with_valid_credentials(self, reset_app):
        """
        TC-006 | P0 | Functional
        Verify an existing user can sign in successfully.
        """
        onboarding = OnboardingPage(reset_app)
        home = HomePage(reset_app)

        onboarding.complete_sign_in(VALID_EMAIL, VALID_PASSWORD)

        assert home.is_home_screen_displayed(), (
            "Home screen not shown after valid sign-in."
        )

    # ── TC-007: Apple SSO button visible ──────────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p1
    def test_apple_sso_button_is_visible_on_sign_up(self, reset_app):
        """
        TC-007 | P1 | Functional
        Verify 'Sign in with Apple' button appears on the sign-up screen.
        Apple requires this for apps with social login (App Store guideline).
        """
        onboarding = OnboardingPage(reset_app)

        onboarding.tap_get_started()
        onboarding.tap_sign_up()

        assert onboarding.is_element_visible(onboarding.APPLE_SSO_BUTTON), (
            "'Sign in with Apple' button is missing on sign-up screen. "
            "This violates Apple App Store guidelines and may cause rejection."
        )

    # ── TC-008: Password mismatch validation ───────────────────────────────────

    @pytest.mark.functional
    @pytest.mark.priority_p1
    def test_sign_up_password_mismatch_shows_error(self, reset_app):
        """
        TC-008 | P1 | Functional
        Verify that mismatching password and confirm-password shows an error.
        """
        onboarding = OnboardingPage(reset_app)

        onboarding.tap_get_started()
        onboarding.tap_sign_up()
        onboarding.enter_email(VALID_EMAIL)
        onboarding.enter_password(VALID_PASSWORD)
        onboarding.enter_confirm_password("DifferentPassword@999")
        onboarding.tap_submit()

        assert onboarding.is_error_displayed(), (
            "No error shown when password and confirm password don't match."
        )
