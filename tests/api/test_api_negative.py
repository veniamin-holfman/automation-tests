import requests


def test_github_api_404():
    url = "https://api.github.com/this-endpoint-should-not-exist"
    r = requests.get(url)

    assert r.status_code == 404
