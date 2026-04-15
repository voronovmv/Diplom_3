import os


def _normalize_base_url(url: str) -> str:
    return url if url.endswith("/") else f"{url}/"


BASE_URL = _normalize_base_url(
    os.getenv("BASE_URL", "https://stellarburgers.education-services.ru/")
)
API_URL = f"{BASE_URL}api/"
WAIT_TIMEOUT = int(os.getenv("WAIT_TIMEOUT", "20"))
TEST_USER_PASSWORD = "Password_123!"
