from selenium.webdriver.common.by import By


class MainPageLocators:
    PAGE_TITLE = (
        By.CSS_SELECTOR,
        "section[class*='BurgerIngredients_ingredients'] > h1",
    )
    CONSTRUCTOR_DROP_AREA = (
        By.CSS_SELECTOR,
        "section[class*='BurgerConstructor_basket']",
    )
    PLACE_ORDER_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'BurgerConstructor_basket')]"
        "//button[text()='\u041e\u0444\u043e\u0440\u043c\u0438\u0442\u044c \u0437\u0430\u043a\u0430\u0437']",
    )

    @staticmethod
    def ingredient_card(ingredient_name_literal: str):
        return (
            By.XPATH,
            "//section[contains(@class, 'BurgerIngredients_ingredients')]"
            "//a[contains(@class, 'BurgerIngredient_ingredient') and "
            "contains(@href, '/ingredient/') and .//p[contains(@class, "
            "'BurgerIngredient_ingredient__text') and text()="
            f"{ingredient_name_literal}]]",
        )

    @staticmethod
    def ingredient_counter(ingredient_name_literal: str):
        return (
            By.XPATH,
            "//section[contains(@class, 'BurgerIngredients_ingredients')]"
            "//a[contains(@class, 'BurgerIngredient_ingredient') and "
            "contains(@href, '/ingredient/') and .//p[contains(@class, "
            "'BurgerIngredient_ingredient__text') and text()="
            f"{ingredient_name_literal}]]//p[contains(@class, 'counter_counter__num')]",
        )
