from selenium.webdriver.common.by import By


class LoginPageLocators:
    PAGE_TITLE = (
        By.XPATH,
        "//*[self::h1 or self::h2][normalize-space()='\u0412\u0445\u043e\u0434']",
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
        "//button[normalize-space()='\u0412\u043e\u0439\u0442\u0438']",
    )
