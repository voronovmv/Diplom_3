import allure

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
        self.wait.until(lambda _: self.get_completed_all_time() > previous_value)

    @allure.step("Дождаться увеличения счётчика «Выполнено за сегодня»")
    def wait_for_today_counter_growth(self, previous_value: int) -> None:
        self.wait.until(lambda _: self.get_completed_today() > previous_value)

    @allure.step("Дождаться появления заказа {order_number} в блоке «В работе»")
    def wait_for_order_in_progress(self, order_number: str) -> None:
        locator = self._order_in_progress_locator(order_number)
        self.wait_until_visible(locator)

    @allure.step("Проверить, что заказ {order_number} отображается в блоке «В работе»")
    def is_order_in_progress_visible(self, order_number: str) -> bool:
        return self.is_visible(self._order_in_progress_locator(order_number))

    def _order_in_progress_locator(self, order_number: str):
        normalized_order_number = order_number.lstrip("0") or "0"
        padded_order_number = normalized_order_number.zfill(7)
        variants = {order_number, normalized_order_number, padded_order_number}
        return OrderFeedPageLocators.order_in_progress(
            [self.xpath_literal(value) for value in variants]
        )

    def _read_counter(self, locator) -> int:
        raw_value = "".join(filter(str.isdigit, self.get_text(locator)))
        return int(raw_value) if raw_value else 0
