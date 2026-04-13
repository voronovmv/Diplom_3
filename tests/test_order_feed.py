import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.order_feed_page import OrderFeedPage


@allure.epic("UI Stellar Burgers")
@allure.feature("Лента заказов")
class TestOrderFeed:
    @staticmethod
    def _login_and_open_feed(driver, user):
        main_page = LoginPage(driver).open_page().login_as(user)
        return main_page.click_order_feed()

    @staticmethod
    def _create_order(main_page: MainPage) -> str:
        main_page.add_ingredient_to_constructor(MainPage.DEFAULT_BUN)
        main_page.add_ingredient_to_constructor(MainPage.DEFAULT_FILLING)
        modal = main_page.place_order()
        order_number = modal.get_order_number()
        modal.close()
        return order_number

    @allure.title("После создания нового заказа счётчик «Выполнено за всё время» увеличивается")
    @allure.description(
        "После оформления нового заказа общий счётчик выполненных заказов должен увеличиться."
    )
    def test_all_time_counter_increases_after_order_creation(self, driver, registered_user):
        order_feed_page = self._login_and_open_feed(driver, registered_user)
        all_time_before = order_feed_page.get_completed_all_time()

        self._create_order(order_feed_page.click_constructor())

        updated_feed = OrderFeedPage(driver).open_page().wait_for_all_time_counter_growth(
            all_time_before
        )

        assert updated_feed.get_completed_all_time() > all_time_before

    @allure.title("После создания нового заказа счётчик «Выполнено за сегодня» увеличивается")
    @allure.description(
        "После оформления нового заказа дневной счётчик выполненных заказов должен увеличиться."
    )
    def test_today_counter_increases_after_order_creation(self, driver, registered_user):
        order_feed_page = self._login_and_open_feed(driver, registered_user)
        today_before = order_feed_page.get_completed_today()

        self._create_order(order_feed_page.click_constructor())

        updated_feed = OrderFeedPage(driver).open_page().wait_for_today_counter_growth(
            today_before
        )

        assert updated_feed.get_completed_today() > today_before

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    @allure.description(
        "Номер оформленного заказа должен отображаться в колонке «В работе»."
    )
    def test_created_order_appears_in_progress_section(self, driver, registered_user):
        order_feed_page = self._login_and_open_feed(driver, registered_user)

        order_number = self._create_order(order_feed_page.click_constructor())

        OrderFeedPage(driver).open_page().wait_for_order_in_progress(order_number)
