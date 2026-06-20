from playwright.sync_api import Page

def test_playwright_main(playwright):
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.goto("https://google.com")



def test_playwright(page:Page):

    page.goto("https://google.com")

