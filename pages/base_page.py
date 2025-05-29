# pages/base_page.py
from playwright.sync_api import Page, expect, Locator
import re  # For regex in URLs or text matching


class BasePage:
    def __init__(self, page: Page):
        self.page = page
        self.base_url = "https://www.oprah.com/"
        self.cookie_agree_button = self.page.get_by_role("button", name="AGREE TO ALL", exact=True)

    def goto(self, url: str):
        """Navigates to a given URL."""
        print(f"DEBUG: Navigating to URL: {url}")
        self.page.goto(url, wait_until='domcontentloaded', timeout=60000)
        print(f"DEBUG: Successfully loaded page: {self.page.url}")

    def dismiss_cookie_banner(self):
        """Attempts to dismiss the cookie consent banner if present."""
        print("DEBUG: Checking for cookie consent banner...")
        try:
            # Wait short time for the button to appear; it's okay if it doesn't.
            expect(self.cookie_agree_button).to_be_visible(timeout=7000)
            print("DEBUG: Cookie 'AGREE TO ALL' button found. Clicking it...")
            self.cookie_agree_button.click(timeout=5000)
            print("DEBUG: Cookie 'AGREE TO ALL' button clicked.")
            # Wait for the button to disappear
            expect(self.cookie_agree_button).not_to_be_visible(timeout=5000)
            print("DEBUG: Cookie banner dismissed successfully.")
        except Exception as e:
            print(f"DEBUG: Cookie banner not found or could not be dismissed within timeout: {e}. Proceeding...")
            # Optional: self.page.screenshot(path="debug_cookie_banner_not_dismissed.png", full_page=True)

    def verify_current_url(self, expected_url_regex: str):
        """Verifies the current page URL matches a regex."""
        print(f"DEBUG: Verifying current URL matches regex: '{expected_url_regex}'...")
        expect(self.page).to_have_url(re.compile(expected_url_regex), timeout=15000)
        print(f"DEBUG: Current URL '{self.page.url}' verified.")

    def verify_element_visible(self, locator_description: str, locator: Locator):
        """Verifies a given locator is visible on the page."""
        print(f"DEBUG: Verifying '{locator_description}' is visible...")
        expect(locator).to_be_visible(timeout=10000)
        print(f"DEBUG: '{locator_description}' is visible.")
