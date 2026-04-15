from selenium.webdriver.common.by import By


class BasePageLocators:
    CONSTRUCTOR_LINK = (
        By.XPATH,
        "//nav[contains(@class, 'AppHeader_header__nav')]"
        "//ul[contains(@class, 'AppHeader_header__list')]"
        "//a[@href='/' and .//p[text()='\u041a\u043e\u043d\u0441\u0442\u0440\u0443\u043a\u0442\u043e\u0440']]",
    )
    ORDER_FEED_LINK = (
        By.XPATH,
        "//nav[contains(@class, 'AppHeader_header__nav')]"
        "//ul[contains(@class, 'AppHeader_header__list')]"
        "//a[@href='/feed' and .//p[text()='\u041b\u0435\u043d\u0442\u0430 \u0417\u0430\u043a\u0430\u0437\u043e\u0432']]",
    )
    MODAL_OVERLAY = (
        By.CSS_SELECTOR,
        "div[class*='Modal_modal_overlay']",
    )
