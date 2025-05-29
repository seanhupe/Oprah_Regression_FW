# conftest.py

import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    """
    Sets up a Playwright browser instance for the entire test session.
    Runs in headed mode (visible browser) with a slight delay for stability.
    """
    print("\n--- conftest.py: Setting up browser ---")
    with sync_playwright() as p:
        # Running in headed mode (headless=False) with slow_mo=500 (0.5 second delay per action)
        _browser = p.chromium.launch(headless=False, slow_mo=500)
        print("--- conftest.py: Browser launched with headless=False, slow_mo=500 ---")
        yield _browser
        _browser.close()
    print("--- conftest.py: Browser closed ---")

@pytest.fixture(scope="function")
def page(browser):
    """
    Sets up a new Playwright page (tab) for each test function.
    Sets a default timeout for Playwright actions.
    """
    _page = browser.new_page()
    _page.set_default_timeout(10000) # Default 10 seconds for actions
    yield _page
    _page.close()

@pytest.fixture(scope="session")
def base_url():
    """
    Provides the base URL as a fixture.
    """
    return "https://www.oprah.com"