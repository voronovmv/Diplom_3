import allure

from locators.modals_locators import IngredientDetailsModalLocators
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
        main_page.open_ingredient_details(MainPage.DEFAULT_SAUCE)
        modal.wait_until_opened()

        assert modal.is_visible(IngredientDetailsModalLocators.MODAL_TITLE)
        assert modal.get_ingredient_name() == MainPage.DEFAULT_SAUCE

    @allure.title("Всплывающее окно закрывается кликом по крестику")
    @allure.description("После клика по крестику модальное окно ингредиента скрывается.")
    def test_close_ingredient_details_modal(self, driver):
        main_page = MainPage(driver)
        modal = IngredientDetailsModal(driver)

        main_page.open_page()
        main_page.open_ingredient_details(MainPage.DEFAULT_SAUCE)
        modal.wait_until_opened()
        modal.close()

        assert not modal.is_visible(IngredientDetailsModalLocators.MODAL_TITLE)
