from uuid import uuid4

import allure
import requests

from config import API_URL, TEST_USER_PASSWORD


def generate_user_data() -> dict[str, str]:
    suffix = uuid4().hex[:10]
    return {
        "name": f"autotest_{suffix}",
        "email": f"autotest_{suffix}@example.com",
        "password": TEST_USER_PASSWORD,
    }


@allure.step("Создать пользователя через API")
def register_user(user_data: dict[str, str]) -> str:
    response = requests.post(
        f"{API_URL}auth/register",
        json=user_data,
        headers={"Content-Type": "application/json"},
        timeout=20,
    )
    assert response.status_code == 200, (
        "Не удалось создать пользователя. "
        f"Status code: {response.status_code}, body: {response.text}"
    )
    return response.json()["accessToken"]


@allure.step("Удалить пользователя через API")
def delete_user(access_token: str | None) -> None:
    if not access_token:
        return

    response = requests.delete(
        f"{API_URL}auth/user",
        headers={"Authorization": access_token},
        timeout=20,
    )
    assert response.status_code in (200, 202), (
        "Не удалось удалить пользователя. "
        f"Status code: {response.status_code}, body: {response.text}"
    )
