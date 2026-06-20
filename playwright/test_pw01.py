from playwright.sync_api import Playwright, Page

# def test_first(playwright):
#     browser = playwright.chromium.launch(headless=False)
#     context = browser.new_context()
#     page = context.new_page()
#     page.goto("https://google.com")

def test_playwrightShortcut(page):
    page.goto("https://youtube.com")

