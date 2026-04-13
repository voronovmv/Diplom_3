import allure
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):
    PAGE_TITLE = (
        By.XPATH,
        "//*[self::h1 or self::h2][normalize-space()='Вход']",
    )
    EMAIL_INPUT = (
        By.XPATH,
        "//input[@type='text' or @type='email' or @name='name']",
    )
    PASSWORD_INPUT = (
        By.XPATH,
        "//input[@type='password']",
    )
    LOGIN_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='Войти']",
    )

    @allure.step("Открыть страницу логина")
    def open_page(self):
        self.open("login")
        self.wait_until_loaded()
        return self

    def wait_until_loaded(self):
        self.wait_until_visible(self.PAGE_TITLE)
        return self

    @allure.step("Авторизоваться пользователем")
    def login_as(self, user: dict[str, str]):
        from pages.main_page import MainPage

        self.type(self.EMAIL_INPUT, user["email"])
        self.type(self.PASSWORD_INPUT, user["password"])
        self.click(self.LOGIN_BUTTON)
        page = MainPage(self.driver)
        page.wait_until_loaded()
        return page
