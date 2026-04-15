from selenium.webdriver.common.by import By


class IngredientDetailsModalLocators:
    MODAL_TITLE = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]"
        "[.//h2[text()='\u0414\u0435\u0442\u0430\u043b\u0438 \u0438\u043d\u0433\u0440\u0435\u0434\u0438\u0435\u043d\u0442\u0430']]"
        "//h2[text()='\u0414\u0435\u0442\u0430\u043b\u0438 \u0438\u043d\u0433\u0440\u0435\u0434\u0438\u0435\u043d\u0442\u0430']",
    )
    INGREDIENT_NAME = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]"
        "[.//h2[text()='\u0414\u0435\u0442\u0430\u043b\u0438 \u0438\u043d\u0433\u0440\u0435\u0434\u0438\u0435\u043d\u0442\u0430']]"
        "//p[contains(@class, 'text_type_main-medium')][last()]",
    )
    CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]"
        "[.//h2[text()='\u0414\u0435\u0442\u0430\u043b\u0438 \u0438\u043d\u0433\u0440\u0435\u0434\u0438\u0435\u043d\u0442\u0430']]"
        "//button[contains(@class, 'Modal_modal__close')]",
    )


class OrderDetailsModalLocators:
    ORDER_IDENTIFIER_LABEL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]"
        "[.//p[text()='\u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043a\u0430\u0437\u0430']]"
        "//p[text()='\u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043a\u0430\u0437\u0430']",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]"
        "[.//p[text()='\u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043a\u0430\u0437\u0430']]"
        "//h2[contains(@class, 'Modal_modal__title')]",
    )
    ORDER_ACCEPTED_TEXT = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]"
        "[.//p[text()='\u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043a\u0430\u0437\u0430']]"
        "//p[text()='\u0412\u0430\u0448 \u0437\u0430\u043a\u0430\u0437 \u043d\u0430\u0447\u0430\u043b\u0438 \u0433\u043e\u0442\u043e\u0432\u0438\u0442\u044c']",
    )
    CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal')]"
        "[.//p[text()='\u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043a\u0430\u0437\u0430']]"
        "//button[contains(@class, 'Modal_modal__close')]",
    )
