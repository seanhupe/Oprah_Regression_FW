# pages/base_page.py
import re
import time
from playwright.sync_api import Page, expect, TimeoutError as PlaywrightTimeoutError, Locator

class BasePage:
    def __init__(self, page: Page):
        self.page = page

    def goto(self, url: str):
        """
        Navigates to a given URL and waits for the page to load,
        with increased timeout and error handling.
        """
        print(f"DEBUG: Navigating to URL: {url}")
        try:
            # Wait for 'load' state first, which means basic HTML and resources are loaded
            self.page.goto(url, wait_until="load", timeout=90000) # Increased timeout significantly
            print(f"DEBUG: Page loaded to '{url}' (load state).")

            # Optional: wait for 'networkidle' if the page has lots of dynamic content
            # This can be flaky, so we'll put it in a try-except
            try:
                self.page.wait_for_load_state("networkidle", timeout=30000) # Give it 30 more seconds for network to idle
                print(f"DEBUG: Page reached 'networkidle' state for '{url}'.")
            except PlaywrightTimeoutError:
                print(f"WARNING: Page '{url}' did not reach 'networkidle' state within 30s, proceeding anyway.")

        except PlaywrightTimeoutError as e:
            print(f"ERROR: Navigation to {url} timed out after 90s: {e}")
            self.page.screenshot(path="failed_goto_timeout.png", full_page=True)
            raise AssertionError(f"Failed to navigate to {url}: {e}. Check failed_goto_timeout.png")
        except Exception as e:
            print(f"ERROR: An unexpected error occurred during navigation to {url}: {e}")
            self.page.screenshot(path="failed_goto_general_error.png", full_page=True)
            raise AssertionError(f"Failed to navigate to {url} due to unexpected error: {e}. Check failed_goto_general_error.png")

    def dismiss_cookie_banner(self):
        """
        Attempts to dismiss the cookie banner if it appears.
        """
        print("DEBUG: Checking for cookie banner...")
        try:
            cookie_accept_button = self.page.locator("#onetrust-accept-btn-handler")
            # Wait for the cookie banner to be visible and then click it
            cookie_accept_button.wait_for(state='visible', timeout=10000)
            cookie_accept_button.click(timeout=5000)
            print("DEBUG: Cookie banner dismissed.")
            # Wait for banner to disappear
            cookie_accept_button.wait_for(state='hidden', timeout=5000)
        except PlaywrightTimeoutError:
            print("DEBUG: Cookie banner did not appear within timeout, or already dismissed.")
        except Exception as e:
            print(f"WARNING: An error occurred while trying to dismiss cookie banner: {e}")
            # Don't fail the test for this, but log the warning

    def verify_element_visible(self, element_name: str, locator: Locator, timeout: int = 20000):
        """
        Verifies if an element is visible on the page within a given timeout.
        """
        print(f"DEBUG: Verifying visibility of '{element_name}'...")
        try:
            locator.wait_for(state="visible", timeout=timeout)
            print(f"DEBUG: '{element_name}' is visible.")
        except PlaywrightTimeoutError:
            self.page.screenshot(path=f"failed_to_see_{element_name.replace(' ', '_')}.png", full_page=True)
            raise AssertionError(f"'{element_name}' was not visible within {timeout}ms. Check screenshot.")
        except Exception as e:
            self.page.screenshot(path=f"failed_to_see_{element_name.replace(' ', '_')}_unexpected.png", full_page=True)
            raise AssertionError(f"An unexpected error occurred while verifying '{element_name}': {e}. Check screenshot.")