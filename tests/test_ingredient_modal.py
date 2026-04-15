import allure

from data.ingredient_names import DEFAULT_SAUCE_NAME
from pages.main_page import MainPage
from pages.modals import IngredientDetailsModal


@allure.epic("UI Stellar Burgers")
@allure.feature("Модальное окно ингредиента")
class TestIngredientModal:
    @allure.title("Клик по ингредиенту открывает всплывающее окно с деталями")
    @allure.description(
        "После клика по карточке ингредиента отображается модальное окно с деталями выбранного ингредиента."
    )
    def test_open_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        modal = IngredientDetailsModal(driver)

        main_page.open_page()
        main_page.open_ingredient_details(DEFAULT_SAUCE_NAME)
        modal.wait_until_opened()

        assert modal.get_ingredient_name() == DEFAULT_SAUCE_NAME

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @allure.description("После клика по крестику модальное окно ингредиента скрывается.")
    def test_close_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        modal = IngredientDetailsModal(driver)

        main_page.open_page()
        main_page.open_ingredient_details(DEFAULT_SAUCE_NAME)
        modal.wait_until_opened()
        modal.close()

        assert not modal.is_opened()
