import allure

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):
    @allure.step("Открыть страницу логина")
    def open_page(self) -> None:
        self.open("login")
        self.wait_until_loaded()

    def wait_until_loaded(self) -> None:
        self.wait_until_visible(LoginPageLocators.PAGE_TITLE)

    @allure.step("Авторизоваться пользователем")
    def login_as(self, user: dict[str, str]) -> None:
        self.type(LoginPageLocators.EMAIL_INPUT, user["email"])
        self.type(LoginPageLocators.PASSWORD_INPUT, user["password"])
        self.click(LoginPageLocators.LOGIN_BUTTON)
