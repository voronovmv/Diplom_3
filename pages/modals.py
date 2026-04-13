import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class IngredientDetailsModal(BasePage):
    MODAL_TITLE = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//h2[normalize-space()='Детали ингредиента']",
    )
    INGREDIENT_NAME = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//p[contains(@class, 'text_type_main-medium')]",
    )
    CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//button",
    )

    @allure.step("Дождаться открытия модального окна ингредиента")
    def wait_until_opened(self):
        self.wait_until_visible(self.MODAL_TITLE)
        return self

    @allure.step("Получить название ингредиента в модальном окне")
    def get_ingredient_name(self) -> str:
        return self.get_text(self.INGREDIENT_NAME)

    @allure.step("Закрыть модальное окно ингредиента")
    def close(self) -> None:
        self.click(self.CLOSE_BUTTON)
        self.wait_until_invisible(self.MODAL_TITLE)


class OrderDetailsModal(BasePage):
    ORDER_IDENTIFIER_LABEL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//p[normalize-space()='идентификатор заказа']",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//p[normalize-space()='идентификатор заказа']/preceding-sibling::h2[1]",
    )
    ORDER_ACCEPTED_TEXT = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//*[contains(normalize-space(), 'Ваш заказ начали готовить')]",
    )
    CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//button",
    )

    @allure.step("Дождаться открытия модального окна заказа")
    def wait_until_opened(self):
        self.wait_until_visible(self.ORDER_IDENTIFIER_LABEL)
        self.wait_until_visible(self.ORDER_ACCEPTED_TEXT)
        return self

    @allure.step("Получить номер заказа")
    def get_order_number(self) -> str:
        self.wait.until(
            lambda _: (
                self.get_text(self.ORDER_NUMBER).replace(" ", "").isdigit()
                and "".join(filter(str.isdigit, self.get_text(self.ORDER_NUMBER))) != "9999"
            )
        )
        return "".join(filter(str.isdigit, self.get_text(self.ORDER_NUMBER)))

    @allure.step("Закрыть модальное окно заказа")
    def close(self) -> None:
        self.click(self.CLOSE_BUTTON)
        self.wait_until_invisible(self.ORDER_IDENTIFIER_LABEL)
        self.wait_for_overlays_to_disappear()
