def test_github_title(page):
    page.goto("https://github.com", wait_until="domcontentloaded")

    title = page.title()
    assert title, "Page title should not be empty"
    assert "GitHub" in title, f"Expected 'GitHub' in title, got: {title}"


def test_github_url(page):
    page.goto("https://github.com", wait_until="domcontentloaded")
    assert page.url.startswith(
        "https://github.com"
    ), f"Expected URL after navigation: {page.url}"
