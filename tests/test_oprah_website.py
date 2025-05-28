# tests/test_oprah_website.py

import pytest
from playwright.sync_api import expect, Page
import allure
import os
import re

# Import your Page Object
from pages.oprah_home_page import OprahHomePage


# ... (test_get_main_section_links_data_functionality is unchanged) ...

@allure.feature("Flyout Menu - Main Sections")
@allure.story("Iterate and click all Main Section links to verify navigation")
def test_click_and_verify_all_main_section_links(page: Page, base_url: str):
    """
    This test iterates through all main section links in the flyout menu,
    clicks each one, and verifies that the navigation is successful.
    """
    oprah_home_page = OprahHomePage(page)

    print(f"\n--- Test: Navigating to homepage on {base_url} ---")
    with allure.step(f"Navigating to homepage and opening the flyout menu on {base_url}"):
        oprah_home_page.goto_homepage(base_url)
        print("--- Test: Homepage loaded. Opening flyout menu ---")
        oprah_home_page.open_flyout_menu()
        print("--- Test: Flyout menu opened ---")
        #page.wait_for_timeout(3000)

    with allure.step("Extracting all main section links for iteration"):
        links_to_test = oprah_home_page.get_main_section_links_data()
        assert links_to_test, "FAILURE: No main section links found to test."
        print(f"--- Test: Found {len(links_to_test)} links: {links_to_test} ---")
        allure.attach(str(links_to_test), name="Links to be Tested", attachment_type=allure.attachment_type.JSON)

    # --- UPDATED: Define precise expected title patterns based on your error log ---
    expected_title_patterns = {
        "Watch OWN": r"OWN TV Network - Watch OWN TV Shows & Episodes Online",  # Updated from error log
        "TV Schedule": r"OWN TV Schedule",  # This one might pass or might need update
        "Podcasts": r"Listen & Subscribe to Your Favorite Podcasts from OWN | OWN",  # Updated from error log
        "Newsletters": r"Newsletters",  # Updated from error log
        "Books": r"Oprah's Book Club: Complete Reading List & Reviews",  # Updated from error log
        "OWN Your Health": r"OWN Your Health",  # This one might pass or might need update
        "Inspiration": r"Inspiration - Happiness and Self-Help Advice - Oprah\.com",  # Updated from error log
        "Food": r"Food, Recipes, Menus, Cooking Advice and More!- Oprah\.com",  # Updated from error log
        "Home": r"Home Decorating and Home Improvement Ideas - Oprah\.com",  # Updated from error log
        "Fashion": r"Style Tips and Advice - Oprah\.com",
        "Help/FAQ": r"The Oprah Winfrey Network Help Center - FAQs | OWN",
    }
    # --------------------------------------------------------------------------

    failed_navigations = []

    with allure.step("Iterating and clicking each link, then verifying navigation"):
        for index, link_data in enumerate(links_to_test):
            link_text = link_data["text"]
            link_expected_url_part = link_data["url"]

            print(f"\n--- Test: Clicking link {index + 1}: '{link_text}' (URL: {link_expected_url_part}) ---")
            with allure.step(f"Testing link {index + 1}: '{link_text}'"):
                try:
                    oprah_home_page.click_main_section_link(link_text)
                    print(f"--- Test: Clicked '{link_text}'. Waiting for navigation... ---")

                    #page.wait_for_timeout(2000)

                    # Assert URL: Use a robust 'contains' regex for URLs
                    expect(page).to_have_url(re.compile(f".*{re.escape(link_expected_url_part)}.*"), timeout=10000)

                    # Assert Title: Use the defined patterns
                    # We will ensure the pattern is explicitly wrapped in .* if it needs to be a "contains" match
                    # For now, let's try direct exact matches based on the error log.
                    # If it fails, we can revisit a more flexible 'contains' logic.
                    expected_regex_pattern_string = expected_title_patterns.get(link_text,
                                                                                link_text)  # Use the link text as fallback if not in dict

                    # For the title, if we define the exact title in the dictionary, then `re.compile()` will look for an exact match.
                    # If we need a "contains" match for items not in the dictionary, we should use f".*{re.escape(link_text)}.*"
                    # Let's adjust the fallback for `to_have_title` to be more flexible, but use exact matches from the dict for specific ones.

                    # The general fallback pattern: contains the link text (case-insensitive)
                    general_fallback_pattern = re.compile(f".*{re.escape(link_text)}.*", re.IGNORECASE)

                    # The specific pattern from our dictionary, if it exists
                    specific_pattern = expected_title_patterns.get(link_text)

                    # If a specific pattern is provided, compile it. Otherwise, use the general fallback.
                    final_title_regex = re.compile(specific_pattern,
                                                   re.IGNORECASE) if specific_pattern else general_fallback_pattern

                    expect(page).to_have_title(final_title_regex, timeout=10000)
                    # ------------------------------------------------------------------

                    print(f"--- Test: Successfully navigated to {page.url} with title: {page.title()} ---")

                    allure.attach(f"Successfully navigated to URL: {page.url} with title: {page.title()}",
                                  name=f"Success for {link_text}", attachment_type=allure.attachment_type.TEXT)

                    screenshot_name = f"screenshot_navigated_to_{link_text.replace(' ', '_').replace('/', '_')}.png"
                    oprah_home_page.take_screenshot(path=screenshot_name)
                    allure.attach.file(screenshot_name, name=f"Navigated to '{link_text}'",
                                       attachment_type=allure.attachment_type.PNG)
                    if os.path.exists(screenshot_name):
                        os.remove(screenshot_name)

                except Exception as e:
                    error_message = f"FAILURE: Link '{link_text}' (URL: {link_expected_url_part}) failed: {e}"
                    print(f"!!! {error_message} !!!")
                    allure.attach(error_message, name=f"Failed: {link_text}",
                                  attachment_type=allure.attachment_type.TEXT)
                    failed_navigations.append(error_message)

                    screenshot_name = f"FAILED_screenshot_on_{link_text.replace(' ', '_').replace('/', '_')}.png"
                    oprah_home_page.take_screenshot(path=screenshot_name)
                    allure.attach.file(screenshot_name, name=f"FAILED State for '{link_text}'",
                                       attachment_type=allure.attachment_type.PNG)
                    if os.path.exists(screenshot_name):
                        os.remove(screenshot_name)

                finally:
                    print(f"--- Test: Returning to homepage for next link ---")
                    try:
                        oprah_home_page.goto_homepage(base_url)
                        oprah_home_page.open_flyout_menu()
                        #page.wait_for_timeout(1000)
                    except Exception as recovery_e:
                        print(f"!!! CRITICAL: Failed to return to homepage/flyout: {recovery_e} !!!")
                        allure.attach(
                            f"Critical: Failed to return to homepage/flyout after '{link_text}' test: {recovery_e}",
                            name="Recovery Failure", attachment_type=allure.attachment_type.TEXT)
                        pytest.fail(
                            f"CRITICAL: Failed to return to homepage/flyout after '{link_text}' test. Subsequent tests might be unreliable.")

    assert not failed_navigations, f"One or more main section links failed during navigation verification:\n" + "\n".join(
        failed_navigations)