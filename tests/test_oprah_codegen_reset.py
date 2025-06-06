# tests/test_oprah_codegen_reset.py

import pytest
from playwright.sync_api import Page, expect
import time
from pages.base_page import BasePage
from pages.oprah_home_page import OprahHomePage


def test_oprah_menu_navigation_pom_step1(page: Page):
    """
    Test migrating to POM: Uses BasePage for initial setup and OprahHomePage for menu interactions.
    """
    print("\n--- Starting POM Migration Test (OprahHomePage Refined) ---")

    # --- Instantiate Page Objects ---
    base_page = BasePage(page)
    oprah_home_page = OprahHomePage(page)

    # --- Initial Navigation and Cookie Dismissal ---
    base_page.goto("https://www.oprah.com/index.html")
    base_page.dismiss_cookie_banner()

    # A small sleep after cookie banner can sometimes help with site stability
    time.sleep(3)

    # --- Your original codegen steps, now using OprahHomePage methods ---

    # WATCH OWN
    oprah_home_page.open_main_menu()
    oprah_home_page.click_primary_link("Watch OWN")
    expect(page.get_by_role("img", name="All OWN Series")).to_be_visible()
    print("DEBUG: Verified Watch OWN.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # TV SCHEDULE
    oprah_home_page.open_main_menu()
    oprah_home_page.page.get_by_role("link",
                                     name="TV Schedule").click()  # Still raw codegen locator for specific elements
    expect(page.locator(".tve-schedule__logo")).to_be_visible()
    print("DEBUG: Verified TV Schedule.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # PODCASTS
    oprah_home_page.open_main_menu()
    oprah_home_page.click_primary_link("Podcasts")
    expect(page.get_by_role("link", name="Listen & Subscribe to Your")).to_be_visible()
    print("DEBUG: Verified Podcasts.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # NEWSLETTERS
    oprah_home_page.open_main_menu()
    oprah_home_page.click_primary_link("Newsletters")
    expect(page.get_by_role("heading", name="NEWSLETTERS")).to_be_visible()
    print("DEBUG: Verified Newsletters.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # BOOKS
    oprah_home_page.open_main_menu()
    oprah_home_page.page.get_by_role("link", name="Books").click()  # Still raw codegen locator
    expect(page.get_by_text("Latest Book Club Picks")).to_be_visible()
    print("DEBUG: Verified Books.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # OWN YOUR HEALTH
    oprah_home_page.open_main_menu()
    oprah_home_page.click_primary_link("OWN Your Health")
    expect(page.locator("#oyh-nav").get_by_role("link", name="OWN Your Health")).to_be_visible()
    print("DEBUG: Verified OWN Your Health.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # INSPIRATION
    oprah_home_page.open_main_menu()
    oprah_home_page.page.get_by_role("link", name="Inspiration", exact=True).click()  # Still raw codegen locator
    expect(page.locator("#heading").get_by_role("link", name="All Topics")).to_be_visible()
    print("DEBUG: Verified Inspiration.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # FOOD (Now using encapsulated POM method)
    oprah_home_page.click_food_link()  # Use new POM method for Food
    expect(page.get_by_role("link", name="Recipes", exact=True)).to_be_visible()
    print("DEBUG: Verified Food.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # HOME
    oprah_home_page.open_main_menu()
    oprah_home_page.page.get_by_role("link", name="Home", exact=True).click()  # Still raw codegen locator
    expect(page.locator("#heading").get_by_role("link", name="All Topics")).to_be_visible()
    print("DEBUG: Verified Home.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # FASHION
    oprah_home_page.open_main_menu()
    oprah_home_page.page.get_by_role("link", name="Fashion").click()  # Still raw codegen locator
    expect(page.locator("#heading").get_by_role("link", name="All Topics")).to_be_visible()
    print("DEBUG: Verified Fashion.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # HELP/FAQ
    oprah_home_page.open_main_menu()
    oprah_home_page.click_primary_link("Help/FAQ")
    expect(page.get_by_role("heading", name="Frequently Asked Questions")).to_be_visible()
    print("DEBUG: Verified Help/FAQ.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # THE NEVER EVER METS
    oprah_home_page.open_main_menu()
    oprah_home_page.click_favorite_app_link("The Never Ever Mets")
    expect(page.get_by_role("link", name="Watch The Never Ever Mets -")).to_be_visible()
    print("DEBUG: Verified The Never Ever Mets.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # #SOMEBODY'S SON
    oprah_home_page.open_main_menu()
    oprah_home_page.click_favorite_app_link("#Somebody's Son")
    expect(page.get_by_role("link", name="Watch #Somebody's Son -")).to_be_visible()
    print("DEBUG: Verified #Somebody's Son.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # FAMILY OR FIANCE
    oprah_home_page.open_main_menu()
    oprah_home_page.click_favorite_app_link("Family or Fiancé")
    expect(page.get_by_role("link", name="Family or Fiance - Watch Full")).to_be_visible()
    print("DEBUG: Verified Family or Fiancé.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # LOVE & MARRIAGE: DETROIT
    oprah_home_page.open_main_menu()
    oprah_home_page.click_favorite_app_link("Love & Marriage: Detroit")
    expect(page.get_by_role("link", name="Stream Love & Marriage:")).to_be_visible()
    print("DEBUG: Verified Love & Marriage: Detroit.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # READY TO LOVE
    oprah_home_page.open_main_menu()
    oprah_home_page.click_favorite_app_link("Ready to Love")
    expect(page.get_by_role("link", name="Watch Ready to Love - Stream")).to_be_visible()
    print("DEBUG: Verified Ready to Love.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    # LOVE & MARRIAGE: HUNTSVILLE
    oprah_home_page.open_main_menu()
    oprah_home_page.click_favorite_app_link("Love & Marriage: Huntsville")
    expect(page.get_by_role("link", name="Watch Love & Marriage:")).to_be_visible()
    print("DEBUG: Verified Love & Marriage: Huntsville.")
    base_page.goto("https://www.oprah.com/index.html")
    time.sleep(5)

    print("--- Test Completed: All POM-integrated steps executed! ---")
