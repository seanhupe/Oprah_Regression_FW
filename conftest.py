# conftest.py
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="session")
def browser():
    """Provides a Playwright browser instance for the entire test session."""
    with sync_playwright() as p:
        # Launch Chromium in non-headless mode so you can see the browser actions
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture(scope="function")
def page(browser):
    """Provides a fresh Playwright page for each test function."""
    page = browser.new_page()
    yield page
    page.close()
