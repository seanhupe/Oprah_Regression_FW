# pages/oprah_home_page.py

from playwright.sync_api import Page, Locator
from pages.base_page import BasePage

class OprahHomePage(BasePage):
    # Locators
    _MAIN_MENU_BUTTON = "#opennav"
    _MAIN_MENU_BUTTON_FOOD_SPECIAL = "#opennav div" # Specific for Food's special click
    _PRIMARY_LINKS_SECTION = "#primary-links"
    _FAVORITE_APPS_SECTION = "#favorite-apps"

    def __init__(self, page: Page):
        super().__init__(page) # Call the constructor of the BasePage
        self.main_menu_button = page.locator(self._MAIN_MENU_BUTTON)
        self.main_menu_button_food_special = page.locator(self._MAIN_MENU_BUTTON_FOOD_SPECIAL).first # New locator for Food
        self.primary_links_section = page.locator(self._PRIMARY_LINKS_SECTION)
        self.favorite_apps_section = page.locator(self._FAVORITE_APPS_SECTION)


    def open_main_menu(self):
        """
        Opens the main navigation menu.
        """
        print("DEBUG: Opening main menu...")
        self.verify_element_visible("Main Menu Button", self.main_menu_button, timeout=30000)
        self.main_menu_button.click()
        print("DEBUG: Main menu opened.")

    def click_primary_link(self, link_name: str) -> Locator:
        """
        Clicks a link within the primary links section of the flyout menu.
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
        link_locator = self.favorite_apps_section.get_by_role("link", name=app_name, exact=True)
        self.verify_element_visible(f"Favorite app link '{app_name}'", link_locator)
        link_locator.click()
        print(f"DEBUG: Favorite app link '{app_name}' clicked.")
        return link_locator

    def click_food_link(self) -> Locator:
        """
        Special method to open the menu and click the 'Food' link,
        using its specific codegen interaction.
        """
        print("DEBUG: Special interaction to open menu and click 'Food' link.")
        self.verify_element_visible("Food Special Menu Button", self.main_menu_button_food_special, timeout=30000)
        self.main_menu_button_food_special.click()

        food_link_locator = self.page.get_by_role("link", name="Food", exact=True)
        self.verify_element_visible("Food Link (after special open)", food_link_locator)
        food_link_locator.click()
        print("DEBUG: 'Food' link clicked using special interaction.")
        return food_link_locator
