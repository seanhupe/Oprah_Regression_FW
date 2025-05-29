# pages/oprah_home_page.py

import re
import os
from playwright.sync_api import Page, expect


class OprahHomePage:
    def __init__(self, page: Page):
        self.page = page
        self.flyout_menu_button = self.page.locator("#opennav")
        self.flyout_menu_container = self.page.locator("#sitenavmenu")
        self.main_section_links_selector = "nav#sitenavmenu ul.main-sections > li > a"

    def goto_homepage(self, url):
        print(f"DEBUG: Navigating to URL: {url}")
        self.page.goto(url, wait_until='networkidle', timeout=30000)
        print(f"DEBUG: Successfully loaded homepage: {self.page.url}")

    def is_flyout_menu_button_visible(self):
        print("DEBUG: Checking if flyout menu button is visible...")
        expect(self.flyout_menu_button).to_be_visible(timeout=30000)
        print("DEBUG: Flyout menu button IS visible.")
        return True

    def open_flyout_menu(self):
        print("DEBUG: Attempting to open flyout menu...")
        self.flyout_menu_button.click(timeout=10000)
        print("DEBUG: Flyout menu button clicked.")
        try:
            expect(self.page.get_by_role("link", name="TV Schedule")).to_be_visible(timeout=20000)
            print("DEBUG: Flyout menu is visible (via waiting for 'TV Schedule' link).")
        except Exception as e:
            print(f"ERROR: 'TV Schedule' link did not become visible within 20s: {e}")
            self.page.screenshot(path="failed_menu_open_screenshot_get_by_role.png")
            print("DEBUG: Screenshot 'failed_menu_open_screenshot_get_by_role.png' taken.")
            raise

    def get_main_section_links_data(self):
        """
        Extracts the text and href attributes of all main section links in the flyout menu.
        """
        print("DEBUG: Extracting main section links data...")
        # --- CRITICAL CHANGE: INCREASED TIMEOUT for 'attached' state to 20 seconds ---
        # This gives Playwright more time to ensure all elements are in the DOM.
        self.page.locator(self.main_section_links_selector).first.wait_for(state='attached', timeout=20000)  # Was 10000

        links_data = []
        # No change to the .all() part
        for link_element in self.page.locator(self.main_section_links_selector).all():
            text = link_element.text_content().strip()
            href = link_element.get_attribute("href")

            if text and href:
                links_data.append({"text": text, "url": href})
        print(f"DEBUG: Found {len(links_data)} links: {links_data}")
        return links_data

    def click_main_section_link(self, link_text):
        print(f"DEBUG: Attempting to click link: '{link_text}'")
        link_locator = self.page.get_by_role("link", name=link_text, exact=True)

        expect(link_locator).to_be_visible(timeout=5000)
        expect(link_locator).to_be_enabled(timeout=5000)
        link_locator.click()
        print(f"DEBUG: Clicked link: '{link_text}'.")
        self.page.wait_for_load_state('load')

    def take_screenshot(self, path="screenshot.png"):
        print(f"DEBUG: Taking screenshot: {path}")
        self.page.screenshot(path=path)
        print(f"DEBUG: Screenshot saved to {path}")