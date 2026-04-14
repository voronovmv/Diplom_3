import allure

from pages.login_page import LoginPage
from pages.main_page import MainPage
from pages.modals import OrderDetailsModal
from pages.order_feed_page import OrderFeedPage


@allure.epic("UI Stellar Burgers")
@allure.feature("Лента заказов")
class TestOrderFeed:
    @allure.title("После создания нового заказа счётчик «Выполнено за всё время» увеличивается")
    @allure.description(
        "После оформления нового заказа общий счётчик выполненных заказов должен увеличиться."
    )
    def test_all_time_counter_increases_after_order_creation(self, driver, registered_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        order_details_modal = OrderDetailsModal(driver)

        login_page.open_page()
        login_page.login_as(registered_user)
        main_page.wait_until_loaded()
        main_page.click_order_feed_link()
        order_feed_page.wait_until_loaded()

        all_time_before = order_feed_page.get_completed_all_time()

        order_feed_page.click_constructor_link()
        main_page.wait_until_loaded()
        main_page.add_default_order_ingredients()
        main_page.click_place_order()
        order_details_modal.wait_until_opened()
        order_details_modal.close()

        order_feed_page.open_page()
        order_feed_page.wait_for_all_time_counter_growth(all_time_before)

        assert order_feed_page.get_completed_all_time() > all_time_before

    @allure.title("После создания нового заказа счётчик «Выполнено за сегодня» увеличивается")
    @allure.description(
        "После оформления нового заказа дневной счётчик выполненных заказов должен увеличиться."
    )
    def test_today_counter_increases_after_order_creation(self, driver, registered_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        order_details_modal = OrderDetailsModal(driver)

        login_page.open_page()
        login_page.login_as(registered_user)
        main_page.wait_until_loaded()
        main_page.click_order_feed_link()
        order_feed_page.wait_until_loaded()

        today_before = order_feed_page.get_completed_today()

        order_feed_page.click_constructor_link()
        main_page.wait_until_loaded()
        main_page.add_default_order_ingredients()
        main_page.click_place_order()
        order_details_modal.wait_until_opened()
        order_details_modal.close()

        order_feed_page.open_page()
        order_feed_page.wait_for_today_counter_growth(today_before)

        assert order_feed_page.get_completed_today() > today_before

    @allure.title("После оформления заказа его номер появляется в разделе «В работе»")
    @allure.description(
        "Номер оформленного заказа должен отображаться в колонке «В работе»."
    )
    def test_created_order_appears_in_progress_section(self, driver, registered_user):
        login_page = LoginPage(driver)
        main_page = MainPage(driver)
        order_feed_page = OrderFeedPage(driver)
        order_details_modal = OrderDetailsModal(driver)

        login_page.open_page()
        login_page.login_as(registered_user)
        main_page.wait_until_loaded()
        main_page.click_order_feed_link()
        order_feed_page.wait_until_loaded()

        order_feed_page.click_constructor_link()
        main_page.wait_until_loaded()
        main_page.add_default_order_ingredients()
        main_page.click_place_order()
        order_details_modal.wait_until_opened()
        order_number = order_details_modal.get_order_number()
        order_details_modal.close()

        order_feed_page.open_page()
        order_feed_page.wait_for_order_in_progress(order_number)

        assert order_feed_page.is_order_in_progress_visible(order_number)
