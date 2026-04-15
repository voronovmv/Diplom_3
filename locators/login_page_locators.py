from selenium.webdriver.common.by import By


class LoginPageLocators:
    PAGE_TITLE = (
        By.CSS_SELECTOR,
        "div[class*='Auth_login'] h2",
    )
    EMAIL_INPUT = (
        By.XPATH,
        "//form[contains(@class, 'Auth_form')]"
        "//label[text()='Email']/following-sibling::input[@name='name']",
    )
    PASSWORD_INPUT = (
        By.XPATH,
        "//form[contains(@class, 'Auth_form')]"
        "//label[text()='\u041f\u0430\u0440\u043e\u043b\u044c']/following-sibling::input[@type='password']",
    )
    LOGIN_BUTTON = (
        By.XPATH,
        "//div[contains(@class, 'Auth_login')]"
        "//form[contains(@class, 'Auth_form')]"
        "//button[contains(@class, 'button_button') and text()='\u0412\u043e\u0439\u0442\u0438']",
    )
