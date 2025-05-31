# pages/oprah_home_page.py

from playwright.sync_api import Page, Locator
from pages.base_page import BasePage # Import BasePage

class OprahHomePage(BasePage):
    # Locators
    _MAIN_MENU_BUTTON = "#opennav"
    _PRIMARY_LINKS_SECTION = "#primary-links"
    _FAVORITE_APPS_SECTION = "#favorite-apps" # While not used as a parent locator directly, useful for context

    def __init__(self, page: Page):
        super().__init__(page) # Call the constructor of the BasePage
        self.main_menu_button = page.locator(self._MAIN_MENU_BUTTON)
        self.primary_links_section = page.locator(self._PRIMARY_LINKS_SECTION)
        self.favorite_apps_section = page.locator(self._FAVORITE_APPS_SECTION)

    def open_main_menu(self):
        """
        Opens the main navigation menu.
        """
        print("DEBUG: Opening main menu...")
        self.verify_element_visible("Main Menu Button", self.main_menu_button, timeout=30000) # Use BasePage's method
        self.main_menu_button.click()
        print("DEBUG: Main menu opened.")

    def click_primary_link(self, link_name: str) -> Locator:
        """
        Clicks a link within the primary links section of the flyout menu.
        Uses the codegen's robust locator.
        """
        print(f"DEBUG: Attempting to click primary link: '{link_name}'")
        link_locator = self.primary_links_section.get_by_role("link", name=link_name, exact=True)
        self.verify_element_visible(f"Primary link '{link_name}'", link_locator)
        link_locator.click()
        print(f"DEBUG: Primary link '{link_name}' clicked.")
        return link_locator

    def click_favorite_app_link(self, app_name: str) -> Locator:
        """
        Clicks an app link within the favorite-apps section of the flyout menu.
        """
        print(f"DEBUG: Attempting to click favorite app link: '{app_name}'")

        # --- MODIFIED LINE HERE ---
        # Scope the search to the favorite_apps_section to avoid strict mode violation
        link_locator = self.favorite_apps_section.get_by_role("link", name=app_name, exact=True)

        self.verify_element_visible(f"Favorite app link '{app_name}'", link_locator)
        link_locator.click()
        print(f"DEBUG: Favorite app link '{app_name}' clicked.")
        return link_locator