# tests/test_oprah_menu_pom.py (Renaming to reflect POM)

import pytest
# Import your new Page Objects
from pages.oprah_home_page import OprahHomePage
from pages.oprah_section_page import OprahSectionPage


# 'page' fixture is provided by conftest.py

def test_oprah_menu_navigation_and_section_verification(page):
    """
    Tests navigating to Oprah.com, dismissing cookies,
    opening the menu, and navigating to various sections
    and verifying their content using Page Object Model.
    """
    print("\n--- Starting Oprah.com Menu Navigation Test (POM) ---")

    # Initialize Page Objects
    oprah_home = OprahHomePage(page)
    oprah_section = OprahSectionPage(page)

    # Reusable test data
    test_data = {
        "primary_links": {
            "Watch OWN": {"url_regex": r"https://www\.oprah\.com/own/watch-own/?"},
            # Add other primary links here as needed later
        },
        "favorite_apps": {
            "Food": {"url_regex": r"https://www\.oprah\.com/food/?"},
            "The Never Ever Mets": {"url_regex": r"https://www\.oprah\.com/app/the-never-ever-mets/?"},
        },
        "apps_showsites": {
            "All Rise": {"url_regex": r"https://www\.oprah\.com/app/all-rise-the-series\.html/?"},
        }
    }

    # --- Test Flow 1: Watch OWN ---
    oprah_home.goto_homepage()  # Handles navigation and cookies
    oprah_home.open_main_menu()
    oprah_home.click_primary_link("Watch OWN")
    oprah_section.verify_watch_own_page()
    print("Flow 1: 'Watch OWN' navigation and verification successful.")
    page.wait_for_timeout(1000)  # Short pause for visual confirmation

    # --- Test Flow 2: Food ---
    oprah_home.goto_homepage()  # Go back to homepage for a fresh start
    oprah_home.open_main_menu()
    oprah_home.click_favorite_app_link("Food")
    oprah_section.verify_food_page()
    print("Flow 2: 'Food' navigation and verification successful.")
    page.wait_for_timeout(1000)  # Short pause

    # --- Test Flow 3: The Never Ever Mets ---
    oprah_home.goto_homepage()  # Go back to homepage
    oprah_home.open_main_menu()
    oprah_home.click_favorite_app_link("The Never Ever Mets")
    oprah_section.verify_the_never_ever_mets_page()
    print("Flow 3: 'The Never Ever Mets' navigation and verification successful.")
    page.wait_for_timeout(1000)  # Short pause

    # --- Test Flow 4: All Rise ---
    oprah_home.goto_homepage()  # Go back to homepage
    oprah_home.open_main_menu()
    oprah_home.click_app_showsite_link("All Rise")
    oprah_section.verify_all_rise_showsite_page()
    print("Flow 4: 'All Rise' navigation and verification successful.")
    page.wait_for_timeout(1000)  # Short pause

    print("\n--- ALL POM TESTS PASSED: Oprah.com Menu Navigation Framework Demo ---")
    page.wait_for_timeout(3000)  # Final pause
