import allure
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.remote.webdriver import WebDriver
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def create_driver(browser_name: str, headless: bool = False) -> WebDriver:
    if browser_name == "chrome":
        options = ChromeOptions()
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--no-sandbox")
        if headless:
            options.add_argument("--headless=new")
        return _create_chrome_driver(options)

    if browser_name == "firefox":
        options = FirefoxOptions()
        if headless:
            options.add_argument("-headless")
        driver = _create_firefox_driver(options)
        driver.set_window_size(1920, 1080)
        return driver

    raise ValueError(f"Unknown browser: {browser_name}")


def attach_screenshot(driver: WebDriver, name: str = "screenshot") -> None:
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )


def attach_page_source(driver: WebDriver, name: str = "page_source") -> None:
    allure.attach(
        driver.page_source,
        name=name,
        attachment_type=allure.attachment_type.HTML,
    )


def _create_chrome_driver(options: ChromeOptions) -> WebDriver:
    try:
        return webdriver.Chrome(options=options)
    except WebDriverException:
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )


def _create_firefox_driver(options: FirefoxOptions) -> WebDriver:
    try:
        return webdriver.Firefox(options=options)
    except WebDriverException:
        return webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )
