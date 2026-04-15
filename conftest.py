import allure
import pytest

from browser_utils import attach_page_source, attach_screenshot, create_driver
from user_api import delete_user, extract_access_token, generate_user_data, register_user


def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="all",
        choices=("chrome", "firefox", "all"),
        help="Браузер для запуска тестов",
    )
    parser.addoption(
        "--headless",
        action="store_true",
        default=False,
        help="Запуск браузеров в headless-режиме",
    )


def pytest_generate_tests(metafunc):
    if "browser_name" in metafunc.fixturenames:
        browser_option = metafunc.config.getoption("browser")
        browsers = ["chrome", "firefox"] if browser_option == "all" else [browser_option]
        metafunc.parametrize("browser_name", browsers, scope="function")


@pytest.fixture
def driver(browser_name, request):
    driver_instance = create_driver(
        browser_name=browser_name,
        headless=request.config.getoption("headless"),
    )
    allure.dynamic.parameter("browser", browser_name)
    yield driver_instance
    driver_instance.quit()


@pytest.fixture
def registered_user():
    user = generate_user_data()
    registration_response = register_user(user)
    if registration_response.status_code != 200:
        raise RuntimeError(
            "Не удалось создать пользователя для теста. "
            f"Status code: {registration_response.status_code}, "
            f"body: {registration_response.text}"
        )

    access_token = extract_access_token(registration_response)
    if not access_token:
        raise RuntimeError(
            "Не удалось получить access token зарегистрированного пользователя. "
            f"Response body: {registration_response.text}"
        )

    yield user

    delete_response = delete_user(access_token)
    if delete_response and delete_response.status_code not in (200, 202):
        raise RuntimeError(
            "Не удалось удалить тестового пользователя. "
            f"Status code: {delete_response.status_code}, body: {delete_response.text}"
        )


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver")
        if driver_instance:
            attach_screenshot(driver_instance)
            attach_page_source(driver_instance)
