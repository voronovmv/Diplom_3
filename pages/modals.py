import allure

from locators.modals_locators import (
    IngredientDetailsModalLocators,
    OrderDetailsModalLocators,
)
from pages.base_page import BasePage


class IngredientDetailsModal(BasePage):
    @allure.step("Дождаться открытия модального окна ингредиента")
    def wait_until_opened(self) -> None:
        self.wait_until_visible(IngredientDetailsModalLocators.MODAL_TITLE)

    @allure.step("Получить название ингредиента в модальном окне")
    def get_ingredient_name(self) -> str:
        return self.get_text(IngredientDetailsModalLocators.INGREDIENT_NAME)

    @allure.step("Закрыть модальное окно ингредиента")
    def close(self) -> None:
        self.click(IngredientDetailsModalLocators.CLOSE_BUTTON)
        self.wait_until_invisible(IngredientDetailsModalLocators.MODAL_TITLE)


class OrderDetailsModal(BasePage):
    @allure.step("Дождаться открытия модального окна заказа")
    def wait_until_opened(self) -> None:
        self.wait_until_visible(OrderDetailsModalLocators.ORDER_IDENTIFIER_LABEL)
        self.wait_until_visible(OrderDetailsModalLocators.ORDER_ACCEPTED_TEXT)

    @allure.step("Получить номер заказа")
    def get_order_number(self) -> str:
        self.wait.until(
            lambda _: (
                self.get_text(OrderDetailsModalLocators.ORDER_NUMBER)
                .replace(" ", "")
                .isdigit()
                and "".join(
                    filter(
                        str.isdigit,
                        self.get_text(OrderDetailsModalLocators.ORDER_NUMBER),
                    )
                )
                != "9999"
            )
        )
        return "".join(
            filter(str.isdigit, self.get_text(OrderDetailsModalLocators.ORDER_NUMBER))
        )

    @allure.step("Проверить, что модальное окно заказа открыто")
    def is_opened(self) -> bool:
        return self.is_visible(OrderDetailsModalLocators.ORDER_IDENTIFIER_LABEL)

    @allure.step("Закрыть модальное окно заказа")
    def close(self) -> None:
        self.click(OrderDetailsModalLocators.CLOSE_BUTTON)
        self.wait_until_invisible(OrderDetailsModalLocators.ORDER_IDENTIFIER_LABEL)
        self.wait_for_overlays_to_disappear()
