from selenium.common.exceptions import ElementClickInterceptedException, TimeoutException
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

from config import BASE_URL, WAIT_TIMEOUT
from locators.base_page_locators import BasePageLocators


class BasePage:
    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, WAIT_TIMEOUT)

    def open(self, relative_url: str = "") -> None:
        self.driver.get(f"{BASE_URL}{relative_url.lstrip('/')}")

    def click(self, locator: tuple[str, str]) -> None:
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

    def type(self, locator: tuple[str, str], value: str) -> None:
        element = self.wait_until_visible(locator)
        element.clear()
        element.send_keys(value)

    def get_text(self, locator: tuple[str, str]) -> str:
        return self.wait_until_visible(locator).text.strip()

    def wait_until_visible(self, locator: tuple[str, str]) -> WebElement:
        return self.wait.until(EC.visibility_of_element_located(locator))

    def wait_until_invisible(self, locator: tuple[str, str]) -> bool:
        return self.wait.until(EC.invisibility_of_element_located(locator))

    def wait_until_url_contains(self, url_part: str) -> bool:
        return self.wait.until(EC.url_contains(url_part))

    def click_constructor_link(self) -> None:
        self.click(BasePageLocators.CONSTRUCTOR_LINK)

    def click_order_feed_link(self) -> None:
        self.click(BasePageLocators.ORDER_FEED_LINK)

    def scroll_to(self, locator: tuple[str, str]) -> None:
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element,
        )

    def find_elements(self, locator: tuple[str, str]) -> list[WebElement]:
        return self.driver.find_elements(*locator)

    def current_url(self) -> str:
        return self.driver.current_url

    def is_visible(self, locator: tuple[str, str]) -> bool:
        try:
            return self.wait_until_visible(locator).is_displayed()
        except TimeoutException:
            return False

    def wait_for_overlays_to_disappear(self) -> None:
        try:
            self.wait.until(
                EC.invisibility_of_element_located(BasePageLocators.MODAL_OVERLAY)
            )
        except TimeoutException:
            pass

    def drag_and_drop(
        self,
        source_locator: tuple[str, str],
        target_locator: tuple[str, str],
    ) -> None:
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
