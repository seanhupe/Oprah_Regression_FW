# pages/oprah_home_page.py
from playwright.sync_api import Locator
from pages.base_page import BasePage
import re  # For regex in locators/assertions if needed


class OprahHomePage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators for homepage elements
        self.open_nav_button = self.page.locator("#opennav")  # Your generated locator
        self.site_navmenu = self.page.locator("#sitenav_menu")  # Your generated locator for the opened menu

        # Locators for specific sections within the flyout menu
        self.primary_links_section = self.page.locator("#primary-links")
        self.favorite_apps_section = self.page.locator("#favorite-apps")
        self.apps_showsites_section = self.page.locator("#apps-showsites")

    def goto_homepage(self):
        """Navigates to the Oprah.com homepage and dismisses cookies."""
        self.goto(self.base_url + "index.html")  # Use the specific index.html path from your codegen
        self.dismiss_cookie_banner()

    def open_main_menu(self):
        """Clicks the 'Open Nav' button and verifies the menu appears."""
        self.verify_element_visible("Open Nav button", self.open_nav_button)
        print("DEBUG: Clicking 'Open Nav' button...")
        self.open_nav_button.click(timeout=5000)
        print("DEBUG: 'Open Nav' button clicked.")
        self.verify_element_visible("Site Nav Menu", self.site_navmenu)
        print("DEBUG: Site navigation menu is visible.")

    # --- Methods for interacting with specific menu links ---
    def click_primary_link(self, link_name: str) -> Locator:
        """Clicks a link within the primary-links section of the flyout menu."""
        print(f"DEBUG: Clicking '{link_name}' link in primary links section...")
        link_locator = self.primary_links_section.get_by_role("link", name=link_name, exact=True)
        self.verify_element_visible(f"Primary link '{link_name}'", link_locator)
        link_locator.click(timeout=10000)
        print(f"DEBUG: Primary link '{link_name}' clicked.")
        return link_locator  # Return locator for potential verification later if needed

    def click_favorite_app_link(self, app_name: str) -> Locator:
        """Clicks an app link within the favorite-apps section of the flyout menu."""
        print(f"DEBUG: Clicking '{app_name}' link in favorite apps section...")
        link_locator = self.favorite_apps_section.get_by_role("link", name=app_name, exact=True)
        self.verify_element_visible(f"Favorite app link '{app_name}'", link_locator)
        link_locator.click(timeout=10000)
        print(f"DEBUG: Favorite app link '{app_name}' clicked.")
        return link_locator

    def click_app_showsite_link(self, showsite_name: str) -> Locator:
        """Clicks a showsite link within the apps-showsites section of the flyout menu."""
        print(f"DEBUG: Clicking '{showsite_name}' link in apps/showsites section...")
        link_locator = self.apps_showsites_section.get_by_role("link", name=showsite_name, exact=True)
        self.verify_element_visible(f"App/Showsite link '{showsite_name}'", link_locator)
        link_locator.click(timeout=10000)
        print(f"DEBUG: App/Showsite link '{showsite_name}' clicked.")
        return link_locator
