from playwright.sync_api import Page, Locator, expect


class OprahHomePage:
    """
    Page Object for the www.oprah.com homepage.
    Encapsulates locators and actions related to the homepage and its flyout menu.
    """

    def __init__(self, page: Page):
        """
        Initializes the OprahHomePage Page Object with the Playwright Page.
        """
        self.page = page

        # --- LOCATORS FOR THE HOMEPAGE ITSELF ---
        self.oprah_logo: Locator = page.locator("id=oprah-logo")  # The Oprah logo on the main page

        # --- LOCATORS FOR THE FLYOUT MENU ---
        self.flyout_menu_button: Locator = page.locator("id=opennav")  # The button to open the flyout menu

        # IMPORTANT: This is the main container for the entire flyout menu once it's open.
        # You confirmed this highlights everything in the flyout.
        self.flyout_root_container: Locator = page.locator("//div[@id='apps-nav']")

        # This locator finds the specific block/section that contains the 10 main links.
        # You confirmed this highlights the main links section.
        self.main_sections_block: Locator = self.flyout_root_container.locator("//div[@id='primary-links']")

        # This locator finds ALL 'a' (link) tags within the 'main_sections_block'.
        self.main_section_links: Locator = self.main_sections_block.locator("a")

    # --- METHODS TO INTERACT WITH THE PAGE ---

    def goto_homepage(self, base_url: str):
        """
        Navigates to the Oprah.com homepage.
        """
        # The URL is configured in conftest.py, so we just go to the root path
        self.page.goto(base_url)

    def verify_main_page_loaded(self):
        """
        Performs basic assertions to verify the main page has loaded successfully.
        """
        expect(self.oprah_logo).to_be_visible()
        expect(self.page).to_have_title("Oprah.com")  # Or expect.string_containing("Oprah")

    def open_flyout_menu(self):
        """
        Clicks the flyout menu button and waits for the menu to become visible.
        """
        expect(self.flyout_menu_button).to_be_visible()
        self.flyout_menu_button.click()
        # Wait until the main flyout container is visible
        expect(self.flyout_root_container).to_be_visible()

    def get_main_section_links_data(self) -> list[dict]:
        """
        Extracts the text and URL for each main section link in the flyout menu.
        Returns:
            A list of dictionaries, where each dict contains 'text' and 'url'.
        """
        extracted_links = []
        # Ensure the block containing the links is visible before trying to extract from it
        expect(self.main_sections_block).to_be_visible()

        # Get all the link (<a>) elements found by self.main_section_links
        links = self.main_section_links.all()

        for link in links:
            href = link.get_attribute("href")
            text = link.text_content().strip()
            # Only add if both href and text are present and href looks valid
            if href and text and (href.startswith("http") or href.startswith("/")):
                extracted_links.append({"text": text, "url": href})
        return extracted_links

    def click_main_section_link(self, link_text: str):
        """
        Clicks a main section link by its visible text.
        Args:
            link_text: The exact text of the link to click (e.g., "Watch Own").
        """
        # This finds an 'a' tag within the main_sections_block that has the exact text.
        target_link = self.main_sections_block.locator(f"a:has-text(\"{link_text}\")").first
        expect(target_link).to_be_visible()
        target_link.click()

    def take_screenshot(self, path: str):
        """
        Takes a screenshot of the current page.
        Args:
            path: The file path to save the screenshot.
        """
        self.page.screenshot(path=path)

    def get_current_page_title(self) -> str:
        """
        Returns the title of the current page.
        """
        return self.page.title()