from selenium.webdriver.common.by import By


class MainPageLocators:
    PAGE_TITLE = (
        By.XPATH,
        "//h1[normalize-space()='\u0421\u043e\u0431\u0435\u0440\u0438\u0442\u0435 \u0431\u0443\u0440\u0433\u0435\u0440']",
    )
    CONSTRUCTOR_DROP_AREA = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket')]",
    )
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//button[normalize-space()='\u041e\u0444\u043e\u0440\u043c\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437']",
    )

    @staticmethod
    def ingredient_card(ingredient_name_literal: str):
        return (
            By.XPATH,
            "//a[contains(@href, '/ingredient/') and .//*[normalize-space()="
            f"{ingredient_name_literal}]]",
        )

    @staticmethod
    def ingredient_counter(ingredient_name_literal: str):
        return (
            By.XPATH,
            "//a[contains(@href, '/ingredient/') and .//*[normalize-space()="
            f"{ingredient_name_literal}]]//*[contains(@class, 'counter_counter')]",
        )
