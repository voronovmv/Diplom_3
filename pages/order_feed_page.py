import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    PAGE_TITLE = (
        By.XPATH,
        "//*[self::h1 or self::p][normalize-space()='Лента заказов']",
    )
    ALL_TIME_COUNTER = (
        By.XPATH,
        "//*[contains(normalize-space(), 'Выполнено за все время')]/following-sibling::*[1]",
    )
    TODAY_COUNTER = (
        By.XPATH,
        "//*[contains(normalize-space(), 'Выполнено за сегодня')]/following-sibling::*[1]",
    )

    @allure.step("Открыть страницу ленты заказов")
    def open_page(self):
        self.open("feed")
        self.wait_until_loaded()
        return self

    def wait_until_loaded(self):
        self.wait_until_visible(self.PAGE_TITLE)
        return self

    @allure.step("Получить значение счётчика «Выполнено за все время»")
    def get_completed_all_time(self) -> int:
        return self._read_counter(self.ALL_TIME_COUNTER)

    @allure.step("Получить значение счётчика «Выполнено за сегодня»")
    def get_completed_today(self) -> int:
        return self._read_counter(self.TODAY_COUNTER)

    @allure.step("Дождаться увеличения счётчика «Выполнено за все время»")
    def wait_for_all_time_counter_growth(self, previous_value: int):
        self.wait.until(lambda _: self.get_completed_all_time() > previous_value)
        return self

    @allure.step("Дождаться увеличения счётчика «Выполнено за сегодня»")
    def wait_for_today_counter_growth(self, previous_value: int):
        self.wait.until(lambda _: self.get_completed_today() > previous_value)
        return self

    @allure.step("Дождаться появления заказа {order_number} в блоке «В работе»")
    def wait_for_order_in_progress(self, order_number: str):
        normalized_order_number = order_number.lstrip("0") or "0"
        padded_order_number = normalized_order_number.zfill(7)
        variants = {order_number, normalized_order_number, padded_order_number}
        conditions = " or ".join(
            f"normalize-space()={self.xpath_literal(value)}" for value in variants
        )
        locator = (
            By.XPATH,
            "//*[contains(normalize-space(), 'В работе')]/following::*["
            f"{conditions}][1]",
        )
        self.wait_until_visible(locator)
        return self

    def _read_counter(self, locator) -> int:
        raw_value = "".join(filter(str.isdigit, self.get_text(locator)))
        return int(raw_value) if raw_value else 0
