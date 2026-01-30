# automation-tests

Portfolio project: automated tests using **pytest**.

## Project structure

- `tests/`
  - `tests/test_smoke.py` — basic smoke tests
  - `tests/api/`
    - `test_api_smoke.py` — API smoke test (GitHub API)
    - `test_api_negative.py` — API negative test (expects 404)
  - `tests/conftest.py` — shared pytest fixtures (if used)

## Requirements

- Python 3.10+ (you use 3.13 — OK)
- Windows / macOS / Linux
- Internet connection (GitHub API tests)

## Setup

Create and activate virtual environment:

### Windows (PowerShell)
```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1

## Notes
- venv/, __pycache__/, .pytest_cache/ are ignored by git (clean repo)