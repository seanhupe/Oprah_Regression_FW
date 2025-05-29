# tests/test_oprah_website.py

import pytest
import re  # Added for URL matching
from playwright.sync_api import Page, expect
import allure

from pages.oprah_home_page import OprahHomePage


@allure.feature("Flyout Menu Interaction and Navigation")
@allure.story("Verify Homepage Loads, Flyout Menu Opens, and Main Sections are Navigable")
def test_navigate_main_sections_via_flyout_menu(page: Page, base_url: str):
    """
    This test navigates to the Oprah.com homepage, opens the flyout menu,
    extracts all main section links, and then clicks each one sequentially,
    navigating back to the homepage and re-opening the menu for each click.
    """
    oprah_home_page = OprahHomePage(page)

    print(f"\n--- Test: Starting full navigation test on {base_url} ---")
    with allure.step(f"Navigating to homepage: {base_url}"):
        oprah_home_page.goto_homepage(base_url)
        print("--- Test: Homepage navigation completed. ---")

    # The following steps constitute the core of what you stated was working
    # i.e., opening the menu and navigating through the 11 sections.

    with allure.step("Opening the flyout menu and extracting links"):
        oprah_home_page.open_flyout_menu()
        print("--- Test: Flyout menu successfully opened. ---")

        main_section_links = oprah_home_page.get_main_section_links_data()
        print(f"--- Test: Found {len(main_section_links)} main section links. ---")
        assert len(main_section_links) > 0, "No main section links found in the flyout menu."

    # Loop through and click each link
    # We navigate back to the homepage and re-open the menu for each link
    # because clicking a link will take us away from the current page.
    for i, link_data in enumerate(main_section_links):
        link_text = link_data["text"]
        link_url = link_data["url"]

        print(f"\n--- Test: Navigating section {i + 1}/{len(main_section_links)}: '{link_text}' ({link_url}) ---")

        with allure.step(f"Clicking link: '{link_text}' and verifying navigation"):
            oprah_home_page.click_main_section_link(link_text)
            print(f"--- Test: Clicked link '{link_text}'. Current URL: {page.url} ---")

            # Assert that navigation occurred to a URL containing parts of the expected link
            # Using regex to allow for variations in base URL or query parameters
            # Example: check if page.url contains "oprah.com/health" if link_url is "https://www.oprah.com/health"
            expected_url_part = link_url.split('//')[-1]  # Gets "www.oprah.com/health" or "oprah.com/health"
            # Adjusting regex to account for potential redirects to non-www or other subdomains/paths
            expect(page).to_have_url(re.compile(f".*{re.escape(expected_url_part)}.*"), timeout=15000)
            print(f"--- Test: Successfully navigated to {page.url} ---")

        # After navigating to a new page, we must return to the homepage
        # to ensure the hamburger menu button is available to click again for the next iteration.
        if i < len(main_section_links) - 1:  # Don't re-open menu after the last link is clicked
            print("--- Test: Returning to homepage and re-opening flyout menu for next navigation ---")
            oprah_home_page.goto_homepage(base_url)  # Go back to homepage
            oprah_home_page.open_flyout_menu()  # Re-open the menu
            print("--- Test: Flyout menu re-opened for next link. ---")

    print("\n--- Test: All main sections navigation PASSED ---")