import allure

from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage


class MainPage(BasePage):
    @allure.step("Открыть главную страницу")
    def open_page(self) -> None:
        self.open()
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        self.wait_until_visible(MainPageLocators.PAGE_TITLE)

    @allure.step("Открыть детали ингредиента «{ingredient_name}»")
    def open_ingredient_details(self, ingredient_name: str) -> None:
        ingredient_card = MainPageLocators.ingredient_card(
            self.xpath_literal(ingredient_name)
        )
        self.scroll_to(ingredient_card)
        self.click(ingredient_card)

    @allure.step("Добавить ингредиент «{ingredient_name}» в конструктор")
    def add_ingredient_to_constructor(self, ingredient_name: str) -> None:
        ingredient_card = MainPageLocators.ingredient_card(
            self.xpath_literal(ingredient_name)
        )
        self.scroll_to(ingredient_card)
        self.drag_and_drop(ingredient_card, MainPageLocators.CONSTRUCTOR_DROP_AREA)

    @allure.step("Оформить заказ")
    def click_place_order(self) -> None:
        self.click(MainPageLocators.PLACE_ORDER_BUTTON)

    @allure.step("Получить значение счётчика ингредиента «{ingredient_name}»")
    def get_ingredient_counter(self, ingredient_name: str) -> int:
        locator = MainPageLocators.ingredient_counter(
            self.xpath_literal(ingredient_name)
        )
        elements = self.find_elements(locator)
        if not elements:
            return 0

        raw_value = elements[0].text.strip()
        return int(raw_value) if raw_value else 0

    @allure.step("Дождаться увеличения счётчика ингредиента «{ingredient_name}»")
    def wait_for_counter_growth(self, ingredient_name: str, previous_value: int) -> int:
        self.wait.until(
            lambda _: self.get_ingredient_counter(ingredient_name) > previous_value
        )
        return self.get_ingredient_counter(ingredient_name)
