import pytest
from playwright.sync_api import Browser, BrowserContext, Playwright, Page, expect


@pytest.fixture(scope="module")
def other_browser(playwright: Playwright):
    browser:Browser = playwright.webkit.launch()#headless=False)
    yield browser
    browser.close()

@pytest.fixture(scope="module")
def iphone_context(other_browser: Browser, playwright: Playwright):
    context = other_browser.new_context(**playwright.devices["iPhone 13"],)
    yield context
    context.close()

@pytest.fixture(scope="module")
def page_on_iphone(iphone_context: BrowserContext):
    page = iphone_context.new_page()
    yield page
    page.close()

def test_aria_snap(page_on_iphone: Page) -> None:
    page_on_iphone.goto("https://playwright.dev/")
    # Toggle nav bar down to see options
    expect(page_on_iphone.get_by_role("navigation", name="Main").get_by_role("link", name="Node.js")).not_to_be_visible()
    page_on_iphone.get_by_role("button", name="Toggle navigation bar").click()
    # Check if node.js button visible
    expect(page_on_iphone.get_by_role("navigation", name="Main").get_by_role("list")).to_match_aria_snapshot("- button \"Node.js\"")
    page_on_iphone.get_by_role("button", name="Expand the dropdown").click()
    expect(page_on_iphone.get_by_role("navigation", name="Main")).to_match_aria_snapshot("- link \"Python\":\n  - /url: /python/")
    expect(page_on_iphone.get_by_role("navigation", name="Main")).to_contain_text("Python")