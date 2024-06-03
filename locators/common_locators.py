from selenium.webdriver.common.by import By


class CommonLocators:
    # поиск родителя
    parent = (By.XPATH, "..")

    # поиск потомков
    children = (By.XPATH, "*")

    # индикатор занятости
    modal_overlay = (By.XPATH, './/div[@class = "Modal_modal_opened__3ISw4 Modal_modal__P3_V5"]'
                               '/div[@class = "Modal_modal_overlay__x2ZCr"]')
