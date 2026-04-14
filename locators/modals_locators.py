from selenium.webdriver.common.by import By


class IngredientDetailsModalLocators:
    MODAL_TITLE = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//h2[normalize-space()='\u0414\u0435\u0442\u0430\u043b\u0438 \u0438\u043d\u0433\u0440\u0435\u0434\u0438\u0435\u043d\u0442\u0430']",
    )
    INGREDIENT_NAME = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//p[contains(@class, 'text_type_main-medium')]",
    )
    CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//button",
    )


class OrderDetailsModalLocators:
    ORDER_IDENTIFIER_LABEL = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//p[normalize-space()='\u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043a\u0430\u0437\u0430']",
    )
    ORDER_NUMBER = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//p[normalize-space()='\u0438\u0434\u0435\u043d\u0442\u0438\u0444\u0438\u043a\u0430\u0442\u043e\u0440 \u0437\u0430\u043a\u0430\u0437\u0430']/preceding-sibling::h2[1]",
    )
    ORDER_ACCEPTED_TEXT = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//*[contains(normalize-space(), '\u0412\u0430\u0448 \u0437\u0430\u043a\u0430\u0437 \u043d\u0430\u0447\u0430\u043b\u0438 \u0433\u043e\u0442\u043e\u0432\u0438\u0442\u044c')]",
    )
    CLOSE_BUTTON = (
        By.XPATH,
        "//section[contains(@class, 'Modal_modal_opened')]//button",
    )
