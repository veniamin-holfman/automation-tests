from playwright.sync_api import sync_playwright


def test_open_github_homepage():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto("https://github.com", wait_until="domcontentloaded")
        assert "GitHub" in page.title()
        browser.close()
