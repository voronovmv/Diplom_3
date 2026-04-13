from __future__ import annotations

from typing import Tuple

from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL, WAIT_TIMEOUT


Locator = Tuple[str, str]


class BasePage:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[@href='/' and .//*[normalize-space()='Конструктор']]",
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        "//a[contains(@href, '/feed') and .//*[contains(normalize-space(), 'Лента')]]",
    )
    MODAL_OVERLAY = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal_overlay')]",
    )

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    def open(self, relative_url: str = "") -> None:
        self.driver.get(f"{BASE_URL}{relative_url.lstrip('/')}")

    def click(self, locator: Locator) -> None:
        element = self.wait.until(EC.element_to_be_clickable(locator))
        try:
            element.click()
        except ElementClickInterceptedException:
            self.wait_for_overlays_to_disappear()
            try:
                self.wait.until(EC.element_to_be_clickable(locator)).click()
            except ElementClickInterceptedException:
                element = self.wait.until(EC.presence_of_element_located(locator))
                self.driver.execute_script("arguments[0].click();", element)

    def type(self, locator: Locator, value: str) -> None:
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator: Locator) -> str:
        return self.wait_until_visible(locator).text.strip()

    def wait_until_visible(self, locator: Locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_invisible(self, locator: Locator) -> bool:
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_until_url_contains(self, url_part: str) -> bool:
        return self.wait.until(EC.url_contains(url_part))

    def click_constructor(self):
        from pages.main_page import MainPage

        self.click(self.CONSTRUCTOR_LINK)
        page = MainPage(self.driver)
        page.wait_until_loaded()
        return page

    def click_order_feed(self):
        from pages.order_feed_page import OrderFeedPage

        self.click(self.ORDER_FEED_LINK)
        page = OrderFeedPage(self.driver)
        page.wait_until_loaded()
        return page

    def scroll_to(self, locator: Locator) -> None:
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    def is_visible(self, locator: Locator) -> bool:
        try:
            return self.wait_until_visible(locator).is_displayed()
        except TimeoutException:
            return False

    def wait_for_overlays_to_disappear(self) -> None:
        try:
            self.wait.until(EC.invisibility_of_element_located(self.MODAL_OVERLAY))
        except TimeoutException:
            pass

    def drag_and_drop(self, source_locator: Locator, target_locator: Locator) -> None:
        source = self.wait_until_visible(source_locator)
        target = self.wait_until_visible(target_locator)
        self.driver.execute_script(
            """
            const source = arguments[0];
            const target = arguments[1];
            const dataTransfer = new DataTransfer();

            source.dispatchEvent(new DragEvent('dragstart', {bubbles: true, dataTransfer}));
            target.dispatchEvent(new DragEvent('dragenter', {bubbles: true, dataTransfer}));
            target.dispatchEvent(new DragEvent('dragover', {bubbles: true, dataTransfer}));
            target.dispatchEvent(new DragEvent('drop', {bubbles: true, dataTransfer}));
            source.dispatchEvent(new DragEvent('dragend', {bubbles: true, dataTransfer}));
            """,
            source,
            target,
        )

    @staticmethod
    def xpath_literal(value: str) -> str:
        if "'" not in value:
            return f"'{value}'"
        if '"' not in value:
            return f'"{value}"'
        parts = value.split("'")
        return "concat(" + ', "\'", '.join(f"'{part}'" for part in parts) + ")"
