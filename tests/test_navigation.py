import allure

from config import BASE_URL
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.epic("UI Stellar Burgers")
@allure.feature("Навигация")
class TestNavigation:
    @allure.title("Переход по клику на «Конструктор»")
    @allure.description("Пользователь может вернуться в конструктор из ленты заказов.")
    def test_open_constructor_from_order_feed(self, driver):
        order_feed_page = OrderFeedPage(driver).open_page()

        order_feed_page.click_constructor()

        assert driver.current_url.startswith(BASE_URL)
        assert "/feed" not in driver.current_url

    @allure.title("Переход по клику на раздел «Лента заказов»")
    @allure.description("Пользователь может открыть ленту заказов с главной страницы.")
    def test_open_order_feed_from_constructor(self, driver):
        main_page = MainPage(driver).open_page()

        main_page.click_order_feed()

        assert "/feed" in driver.current_url
