import allure
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


def create_driver(browser_name: str, headless: bool = False):
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

    raise ValueError(f"Неизвестный браузер: {browser_name}")


def attach_screenshot(driver, name: str = "screenshot") -> None:
    allure.attach(
        driver.get_screenshot_as_png(),
        name=name,
        attachment_type=allure.attachment_type.PNG,
    )


def attach_page_source(driver, name: str = "page_source") -> None:
    allure.attach(
        driver.page_source,
        name=name,
        attachment_type=allure.attachment_type.HTML,
    )


def _create_chrome_driver(options: ChromeOptions):
    try:
        return webdriver.Chrome(options=options)
    except WebDriverException:
        return webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()),
            options=options,
        )


def _create_firefox_driver(options: FirefoxOptions):
    try:
        return webdriver.Firefox(options=options)
    except WebDriverException:
        return webdriver.Firefox(
            service=FirefoxService(GeckoDriverManager().install()),
            options=options,
        )
