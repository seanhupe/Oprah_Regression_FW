# tests/test_oprah_codegen_reset.py

import pytest
from playwright.sync_api import Page, expect
import time # Needed for the sleep
from pages.base_page import BasePage # <-- NEW: Import BasePage

def test_oprah_menu_navigation_codegen_reset(page: Page):
    """
    Runs the original codegen test, now utilizing BasePage for initial setup,
    to establish a stable baseline.
    """
    print("\n--- Starting Codegen Reset Test (with BasePage) ---")

    # --- Instantiate BasePage ---
    base_page = BasePage(page)

    # --- Use BasePage's goto method ---
    base_page.goto("https://www.oprah.com/index.html")

    # --- Use BasePage's dismiss_cookie_banner method ---
    base_page.dismiss_cookie_banner()

    # --- Explicitly wait for the #opennav button to be visible before clicking ---
    # Keeping this here for now, we'll move it into OprahHomePage later
    print("DEBUG: Waiting for #opennav button to be visible...")
    try:
        page.locator("#opennav").wait_for(state='visible', timeout=30000)
        print("DEBUG: #opennav button is visible.")
        page.locator("#opennav").click()
        print("DEBUG: #opennav button clicked.")
    except Exception as e:
        page.screenshot(path="failed_opennav_click_pom.png", full_page=True)
        raise AssertionError(f"Failed to click #opennav button: {e}. Check failed_opennav_click_pom.png")

    # --- Your original codegen steps, with a sleep after each goto ---

    # WATCH OWN
    page.locator("#primary-links").get_by_role("link", name="Watch OWN").click()
    expect(page.get_by_role("img", name="All OWN Series")).to_be_visible()
    print("DEBUG: Verified Watch OWN.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # TV SCHEDULE
    page.locator("#opennav").click()
    page.get_by_role("link", name="TV Schedule").click()
    expect(page.locator(".tve-schedule__logo")).to_be_visible()
    print("DEBUG: Verified TV Schedule.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # PODCASTS
    page.locator("#opennav").click()
    page.locator("#primary-links").get_by_role("link", name="Podcasts").click()
    expect(page.get_by_role("link", name="Listen & Subscribe to Your")).to_be_visible()
    print("DEBUG: Verified Podcasts.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # NEWSLETTERS
    page.locator("#opennav").click()
    page.locator("#primary-links").get_by_role("link", name="Newsletters").click()
    expect(page.get_by_role("heading", name="NEWSLETTERS")).to_be_visible()
    print("DEBUG: Verified Newsletters.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # BOOKS
    page.locator("#opennav").click()
    page.get_by_role("link", name="Books").click()
    expect(page.get_by_text("Latest Book Club Picks")).to_be_visible()
    print("DEBUG: Verified Books.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # OWN YOUR HEALTH
    page.locator("#opennav").click()
    page.locator("#primary-links").get_by_role("link", name="OWN Your Health").click()
    expect(page.locator("#oyh-nav").get_by_role("link", name="OWN Your Health")).to_be_visible()
    print("DEBUG: Verified OWN Your Health.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # INSPIRATION
    page.locator("#opennav").click()
    page.get_by_role("link", name="Inspiration", exact=True).click()
    expect(page.locator("#heading").get_by_role("link", name="All Topics")).to_be_visible()
    print("DEBUG: Verified Inspiration.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # FOOD (THIS IS THE ONE THAT FAILED BEFORE)
    page.locator("#opennav div").first.click() # Using codegen's specific locator for menu re-open
    page.get_by_role("link", name="Food", exact=True).click() # Using codegen's specific locator
    expect(page.get_by_role("link", name="Recipes", exact=True)).to_be_visible()
    print("DEBUG: Verified Food.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # HOME
    page.locator("#opennav").click()
    page.get_by_role("link", name="Home", exact=True).click()
    expect(page.locator("#heading").get_by_role("link", name="All Topics")).to_be_visible()
    print("DEBUG: Verified Home.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # FASHION
    page.locator("#opennav").click()
    page.get_by_role("link", name="Fashion").click()
    expect(page.locator("#heading").get_by_role("link", name="All Topics")).to_be_visible()
    print("DEBUG: Verified Fashion.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # HELP/FAQ
    page.locator("#opennav").click()
    page.locator("#primary-links").get_by_role("link", name="Help/FAQ").click()
    expect(page.get_by_role("heading", name="Frequently Asked Questions")).to_be_visible()
    print("DEBUG: Verified Help/FAQ.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # THE NEVER EVER METS
    page.locator("#opennav").click()
    page.locator("#favorite-apps").get_by_role("link", name="The Never Ever Mets").click()
    expect(page.get_by_role("link", name="Watch The Never Ever Mets -")).to_be_visible()
    print("DEBUG: Verified The Never Ever Mets.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # #SOMEBODY'S SON
    page.locator("#opennav").click()
    page.get_by_role("link", name="#Somebody's Son").click()
    expect(page.get_by_role("link", name="Watch #Somebody's Son -")).to_be_visible()
    print("DEBUG: Verified #Somebody's Son.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # FAMILY OR FIANCE
    page.locator("#opennav").click()
    page.get_by_role("link", name="Family or Fiancé", exact=True).click()
    expect(page.get_by_role("link", name="Family or Fiance - Watch Full")).to_be_visible()
    print("DEBUG: Verified Family or Fiancé.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # LOVE & MARRIAGE: DETROIT
    page.locator("#opennav").click()
    page.locator("#favorite-apps").get_by_role("link", name="Love & Marriage: Detroit").click()
    expect(page.get_by_role("link", name="Stream Love & Marriage:")).to_be_visible()
    print("DEBUG: Verified Love & Marriage: Detroit.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # READY TO LOVE
    page.locator("#opennav").click()
    page.locator("#favorite-apps").get_by_role("link", name="Ready to Love").click()
    expect(page.get_by_role("link", name="Watch Ready to Love - Stream")).to_be_visible()
    print("DEBUG: Verified Ready to Love.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    # LOVE & MARRIAGE: HUNTSVILLE
    page.locator("#opennav").click()
    page.locator("#favorite-apps").get_by_role("link", name="Love & Marriage: Huntsville").click()
    expect(page.get_by_role("link", name="Watch Love & Marriage:")).to_be_visible()
    print("DEBUG: Verified Love & Marriage: Huntsville.")
    page.goto("https://www.oprah.com/index.html")
    time.sleep(5) # Wait after goto

    print("--- Test Completed: All Codegen steps executed! ---")