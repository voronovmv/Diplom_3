import allure
import pytest

from browser_utils import attach_page_source, attach_screenshot, create_driver
from user_api import delete_user, generate_user_data, register_user


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
    access_token = register_user(user)
    yield user
    delete_user(access_token)


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()
    if report.when == "call" and report.failed:
        driver_instance = item.funcargs.get("driver")
        if driver_instance:
            attach_screenshot(driver_instance)
            attach_page_source(driver_instance)
