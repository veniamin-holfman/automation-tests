def test_github_title(page):
    page.goto("https://github.com", wait_until="domcontentloaded")
    assert "GitHub" in page.title()


def test_github_url(page):
    page.goto("https://github.com", wait_until="domcontentloaded")
    assert page.url.startswith("https://github.com")
