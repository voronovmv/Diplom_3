from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    PAGE_TITLE = (
        By.XPATH,
        "//*[self::h1 or self::p][normalize-space()='\u041b\u0435\u043d\u0442\u0430 \u0437\u0430\u043a\u0430\u0437\u043e\u0432']",
    )
    ALL_TIME_COUNTER = (
        By.XPATH,
        "//*[contains(normalize-space(), '\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e \u0437\u0430 \u0432\u0441\u0435 \u0432\u0440\u0435\u043c\u044f')]/following-sibling::*[1]",
    )
    TODAY_COUNTER = (
        By.XPATH,
        "//*[contains(normalize-space(), '\u0412\u044b\u043f\u043e\u043b\u043d\u0435\u043d\u043e \u0437\u0430 \u0441\u0435\u0433\u043e\u0434\u043d\u044f')]/following-sibling::*[1]",
    )

    @staticmethod
    def order_in_progress(order_number_literals: list[str]):
        conditions = " or ".join(
            f"normalize-space()={value}" for value in order_number_literals
        )
        return (
            By.XPATH,
            "//*[contains(normalize-space(), '\u0412 \u0440\u0430\u0431\u043e\u0442\u0435')]/following::*["
            f"{conditions}][1]",
        )
