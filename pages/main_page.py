import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage
from pages.modals import IngredientDetailsModal, OrderDetailsModal


class MainPage(BasePage):
    PAGE_TITLE = (
        By.XPATH,
        "//h1[normalize-space()='Соберите бургер']",
    )
    CONSTRUCTOR_DROP_AREA = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket')]",
    )
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Оформить заказ']",
    )

    DEFAULT_BUN = "Флюоресцентная булка R2-D3"
    DEFAULT_SAUCE = "Соус Spicy-X"
    DEFAULT_FILLING = "Хрустящие минеральные кольца"

    @allure.step("Открыть главную страницу")
    def open_page(self):
        self.open()
        self.wait_until_loaded()
        return self

    def wait_until_loaded(self):
        self.wait_until_visible(self.PAGE_TITLE)
        return self

    @allure.step("Открыть детали ингредиента «{ingredient_name}»")
    def open_ingredient_details(self, ingredient_name: str) -> IngredientDetailsModal:
        ingredient_card = self._ingredient_card(ingredient_name)
        self.scroll_to(ingredient_card)
        self.click(ingredient_card)
        return IngredientDetailsModal(self.driver).wait_until_opened()

    @allure.step("Добавить ингредиент «{ingredient_name}» в конструктор")
    def add_ingredient_to_constructor(self, ingredient_name: str):
        ingredient_card = self._ingredient_card(ingredient_name)
        self.scroll_to(ingredient_card)
        self.drag_and_drop(ingredient_card, self.CONSTRUCTOR_DROP_AREA)
        return self

    @allure.step("Оформить заказ")
    def place_order(self) -> OrderDetailsModal:
        self.click(self.PLACE_ORDER_BUTTON)
        return OrderDetailsModal(self.driver).wait_until_opened()

    @allure.step("Получить значение счётчика ингредиента «{ingredient_name}»")
    def get_ingredient_counter(self, ingredient_name: str) -> int:
        locator = self._ingredient_counter(ingredient_name)
        elements = self.driver.find_elements(*locator)
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

    def _ingredient_card(self, ingredient_name: str):
        return (
            By.XPATH,
            "//a[contains(@href, '/ingredient/') and .//*[normalize-space()="
            f"{self.xpath_literal(ingredient_name)}]]",
        )

    def _ingredient_counter(self, ingredient_name: str):
        return (
            By.XPATH,
            "//a[contains(@href, '/ingredient/') and .//*[normalize-space()="
            f"{self.xpath_literal(ingredient_name)}]]//*[contains(@class, 'counter_counter')]",
        )
