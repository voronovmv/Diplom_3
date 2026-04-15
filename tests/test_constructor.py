import allure

from data.ingredient_names import DEFAULT_SAUCE_NAME
from pages.main_page import MainPage


@allure.epic("UI Stellar Burgers")
@allure.feature("Конструктор")
class TestConstructor:
    @allure.title("При добавлении ингредиента в заказ счётчик ингредиента увеличивается")
    @allure.description(
        "После добавления ингредиента в конструктор его счётчик на карточке увеличивается."
    )
    def test_ingredient_counter_increases_after_adding_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.open_page()
        counter_before = main_page.get_ingredient_counter(DEFAULT_SAUCE_NAME)

        main_page.add_ingredient_to_constructor(DEFAULT_SAUCE_NAME)
        counter_after = main_page.wait_for_counter_growth(
            DEFAULT_SAUCE_NAME,
            counter_before,
        )

        assert counter_after > counter_before
