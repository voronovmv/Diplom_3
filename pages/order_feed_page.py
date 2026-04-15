import time
from collections.abc import Callable

import allure
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException

from config import WAIT_TIMEOUT
from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage


class OrderFeedPage(BasePage):
    @allure.step("Открыть страницу ленты заказов")
    def open_page(self) -> None:
        self.open("feed")
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        self.wait_until_visible(OrderFeedPageLocators.PAGE_TITLE)

    @allure.step("Получить значение счётчика «Выполнено за все время»")
    def get_completed_all_time(self) -> int:
        return self._read_counter(OrderFeedPageLocators.ALL_TIME_COUNTER)

    @allure.step("Получить значение счётчика «Выполнено за сегодня»")
    def get_completed_today(self) -> int:
        return self._read_counter(OrderFeedPageLocators.TODAY_COUNTER)

    @allure.step("Дождаться увеличения счётчика «Выполнено за все время»")
    def wait_for_all_time_counter_growth(self, previous_value: int) -> None:
        self._wait_for_counter_growth(self.get_completed_all_time, previous_value)

    @allure.step("Дождаться увеличения счётчика «Выполнено за сегодня»")
    def wait_for_today_counter_growth(self, previous_value: int) -> None:
        self._wait_for_counter_growth(self.get_completed_today, previous_value)

    @allure.step("Дождаться появления заказа {order_number} в блоке «В работе»")
    def wait_for_order_in_progress(self, order_number: str) -> None:
        normalized_order_number = self._normalize_order_number(order_number)
        self.wait.until(
            lambda _: normalized_order_number in self.get_orders_in_progress()
        )

    @allure.step("Проверить, что заказ {order_number} отображается в блоке «В работе»")
    def is_order_in_progress_visible(self, order_number: str) -> bool:
        return self._normalize_order_number(order_number) in self.get_orders_in_progress()

    def get_orders_in_progress(self) -> list[str]:
        try:
            return [
                element.text.strip()
                for element in self.find_elements(
                    OrderFeedPageLocators.IN_PROGRESS_ORDER_NUMBERS
                )
                if element.text.strip()
            ]
        except StaleElementReferenceException:
            return []

    def _read_counter(self, locator: tuple[str, str]) -> int:
        raw_value = "".join(filter(str.isdigit, self.get_text(locator)))
        return int(raw_value) if raw_value else 0

    def _wait_for_counter_growth(
        self,
        getter: Callable[[], int],
        previous_value: int,
    ) -> None:
        deadline = time.monotonic() + WAIT_TIMEOUT * 3
        while time.monotonic() < deadline:
            try:
                if getter() > previous_value:
                    return
            except StaleElementReferenceException:
                pass

            self.driver.refresh()
            self.wait_until_loaded()
            time.sleep(1)

        raise TimeoutException("Counter value did not increase within the expected time.")

    @staticmethod
    def _normalize_order_number(order_number: str) -> str:
        return "".join(filter(str.isdigit, order_number)).zfill(7)
