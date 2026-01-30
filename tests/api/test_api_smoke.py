import requests


def test_github_api_status_and_json():
    response = requests.get("https://api.github.com")

    assert response.status_code == 200

    data = response.json()

    assert "current_user_url" in data
    assert "authorizations_url" in data
    assert data["current_user_url"].startswith("https://api.github.com")
