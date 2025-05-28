# conftest.py

import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    """
    Sets up a Playwright browser instance for the entire test session.
    """
    print("\n--- conftest.py: Setting up browser ---")  # <--- ADD THIS
    with sync_playwright() as p:
        _browser = p.chromium.launch(headless=False, slow_mo=0)  # <--- ENSURE slow_mo=1000 (1 second delay)
        print("--- conftest.py: Browser launched with headless=False, slow_mo=1000 ---")  # <--- ADD THIS
        yield _browser
        _browser.close()


@pytest.fixture(scope="function")
def page(browser):
    _page = browser.new_page()
    # Temporarily increase default timeout to give more time for elements to appear
    _page.set_default_timeout(10000)  # Increased timeout to 15 seconds
    yield _page
    _page.close()


@pytest.fixture(scope="session")
def base_url():
    """
    Provides the base URL as a fixture.
    """
    return "https://www.oprah.com"  # Ensure this matches the _page.goto in the page fixture
