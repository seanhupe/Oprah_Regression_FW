# pages/oprah_section_page.py
from playwright.sync_api import Locator
from pages.base_page import BasePage
import re


class OprahSectionPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators for elements commonly found on various section pages
        # Using very generic ones first, then refining based on your codegen's specific assertions

        self.all_own_series_text = self.page.get_by_text("All OWN Series The Never Ever")
        self.recipes_link = self.page.get_by_role("link", name="Recipes", exact=True)
        self.the_never_ever_mets_watch_link = self.page.get_by_role("link", name="Watch The Never Ever Mets -")
        self.all_rise_watch_image = self.page.get_by_role("img", name="Watch All Rise - Stream")

        # Generic page container from your codegen
        self.generic_page_container = self.page.locator(".page")

    # --- Methods for verifying specific section pages ---

    def verify_watch_own_page(self):
        """Verifies elements and URL for the 'Watch OWN' section page."""
        self.verify_current_url(r"https://www\.oprah\.com/own/watch-own/?")  # Adjust regex if needed for exact URL
        self.verify_element_visible("All OWN Series text", self.all_own_series_text)
        print("DEBUG: 'Watch OWN' page verified.")

    def verify_food_page(self):
        """Verifies elements and URL for the 'Food' section page."""
        self.verify_current_url(r"https://www\.oprah\.com/food/?")  # Adjust regex if needed
        self.verify_element_visible("Generic Page Container (.page)", self.generic_page_container)
        self.verify_element_visible("Recipes link on Food page", self.recipes_link)
        print("DEBUG: 'Food' page verified.")

    def verify_the_never_ever_mets_page(self):
        """Verifies elements and URL for 'The Never Ever Mets' app page."""
        # The URL for app pages can be complex, often includes dynamic IDs or parameters.
        # We'll use a broader regex or just rely on element visibility for this one if URL is too volatile.
        self.verify_current_url(r"https://www\.oprah\.com/app/the-never-ever-mets/?")  # Adjust regex if needed
        self.verify_element_visible("Watch The Never Ever Mets link", self.the_never_ever_mets_watch_link)
        print("DEBUG: 'The Never Ever Mets' app page verified.")

    def verify_all_rise_showsite_page(self):
        """Verifies elements and URL for the 'All Rise' showsite page."""
        self.verify_current_url(r"https://www\.oprah\.com/app/all-rise-the-series\.html/?")  # Adjust regex if needed
        self.verify_element_visible("Watch All Rise image", self.all_rise_watch_image)
        print("DEBUG: 'All Rise' showsite page verified.")
