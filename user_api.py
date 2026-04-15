from uuid import uuid4

import allure
import requests
from requests import Response

from config import API_URL, TEST_USER_PASSWORD


def generate_user_data() -> dict[str, str]:
    suffix = uuid4().hex[:10]
    return {
        "name": f"autotest_{suffix}",
        "email": f"autotest_{suffix}@example.com",
        "password": TEST_USER_PASSWORD,
    }


@allure.step("Создать пользователя через API")
def register_user(user_data: dict[str, str]) -> Response:
    return requests.post(
        f"{API_URL}auth/register",
        json=user_data,
        headers={"Content-Type": "application/json"},
        timeout=20,
    )


def extract_access_token(response: Response) -> str | None:
    try:
        return response.json().get("accessToken")
    except ValueError:
        return None


@allure.step("Удалить пользователя через API")
def delete_user(access_token: str | None) -> Response | None:
    if not access_token:
        return None

    return requests.delete(
        f"{API_URL}auth/user",
        headers={"Authorization": access_token},
        timeout=20,
    )
