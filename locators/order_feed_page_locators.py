from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    PAGE_TITLE = (
        By.CSS_SELECTOR,
        "div[class*='OrderFeed_orderFeed'] > h1",
    )
    ALL_TIME_COUNTER = (
        By.XPATH,
        "//div[contains(@class, 'OrderFeed_ordersData')]"
        "//p[text()='Выполнено за все время:']"
        "/following-sibling::p[contains(@class, 'OrderFeed_number')][1]",
    )
    TODAY_COUNTER = (
        By.XPATH,
        "//div[contains(@class, 'OrderFeed_ordersData')]"
        "//p[text()='Выполнено за сегодня:']"
        "/following-sibling::p[contains(@class, 'OrderFeed_number')][1]",
    )
    IN_PROGRESS_ORDER_NUMBERS = (
        By.XPATH,
        "//div[contains(@class, 'OrderFeed_orderStatusBox')]"
        "//p[text()='В работе:']"
        "/following-sibling::ul[contains(@class, 'OrderFeed_orderList')]//li",
    )
