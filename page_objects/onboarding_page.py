"""
onboarding_page.py — Page Object for Speechify's onboarding/login screens.

This represents every action a user can take on the welcome, sign-up,
and sign-in screens of the Speechify iOS app.
"""

from page_objects.base_page import BasePage


class OnboardingPage(BasePage):
    """Handles the Welcome → Sign Up / Sign In flow."""

    # ── Accessibility IDs (set by Speechify's iOS developers) ────────────────
    # These are the labels Appium uses to find buttons and fields on screen.

    GET_STARTED_BUTTON = "getStartedButton"
    SIGN_UP_BUTTON = "signUpButton"
    SIGN_IN_BUTTON = "signInButton"
    EMAIL_FIELD = "emailTextField"
    PASSWORD_FIELD = "passwordTextField"
    CONFIRM_PASSWORD_FIELD = "confirmPasswordTextField"
    SUBMIT_BUTTON = "submitButton"
    GOOGLE_SSO_BUTTON = "continueWithGoogleButton"
    APPLE_SSO_BUTTON = "continueWithAppleButton"
    SKIP_BUTTON = "skipButton"
    ERROR_MESSAGE_LABEL = "errorMessageLabel"
    WELCOME_TITLE = "welcomeTitleLabel"

    # ── Actions ───────────────────────────────────────────────────────────────

    def tap_get_started(self):
        """Tap the 'Get Started' button on the welcome screen."""
        self.tap(self.GET_STARTED_BUTTON)

    def tap_sign_up(self):
        """Navigate to the Sign Up screen."""
        self.tap(self.SIGN_UP_BUTTON)

    def tap_sign_in(self):
        """Navigate to the Sign In screen."""
        self.tap(self.SIGN_IN_BUTTON)

    def enter_email(self, email: str):
        """Type an email address into the email field."""
        self.type_text(self.EMAIL_FIELD, email)

    def enter_password(self, password: str):
        """Type a password into the password field."""
        self.type_text(self.PASSWORD_FIELD, password)

    def enter_confirm_password(self, password: str):
        """Type password again in the confirmation field (sign-up only)."""
        self.type_text(self.CONFIRM_PASSWORD_FIELD, password)

    def tap_submit(self):
        """Tap the Submit/Continue button to complete sign-up or sign-in."""
        self.tap(self.SUBMIT_BUTTON)

    def tap_continue_with_google(self):
        """Tap 'Continue with Google' SSO button."""
        self.tap(self.GOOGLE_SSO_BUTTON)

    def tap_continue_with_apple(self):
        """Tap 'Continue with Apple' SSO button."""
        self.tap(self.APPLE_SSO_BUTTON)

    def tap_skip(self):
        """Tap Skip to bypass onboarding steps."""
        self.tap(self.SKIP_BUTTON)

    # ── Full flows (combining multiple actions) ───────────────────────────────

    def complete_sign_up(self, email: str, password: str):
        """
        Full sign-up flow: get started → sign up → fill form → submit.
        Used by tests that need a logged-in state quickly.
        """
        self.tap_get_started()
        self.tap_sign_up()
        self.enter_email(email)
        self.enter_password(password)
        self.enter_confirm_password(password)
        self.tap_submit()

    def complete_sign_in(self, email: str, password: str):
        """Full sign-in flow: get started → sign in → fill form → submit."""
        self.tap_get_started()
        self.tap_sign_in()
        self.enter_email(email)
        self.enter_password(password)
        self.tap_submit()

    # ── Assertions / State checks ─────────────────────────────────────────────

    def is_welcome_screen_displayed(self) -> bool:
        """Return True if the welcome/onboarding screen is visible."""
        return self.is_element_visible(self.WELCOME_TITLE)

    def get_error_message(self) -> str:
        """Return the text of any error message shown on screen."""
        return self.get_text(self.ERROR_MESSAGE_LABEL)

    def is_error_displayed(self) -> bool:
        """Return True if an error message is currently visible."""
        return self.is_element_visible(self.ERROR_MESSAGE_LABEL, timeout=5)
