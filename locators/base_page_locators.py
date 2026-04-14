from selenium.webdriver.common.by import By


class BasePageLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//a[@href='/' and .//*[normalize-space()='\u041a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440']]",
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        "//a[contains(@href, '/feed') and .//*[contains(normalize-space(), '\u041b\u0435\u043d\u0442\u0430')]]",
    )
    MODAL_OVERLAY = (
        By.XPATH,
        "//div[contains(@class, 'Modal_modal_overlay')]",
    )
