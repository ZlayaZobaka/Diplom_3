from selenium.webdriver.common.by import By


class CommonLocators:
    # поиск родителя
    parent = (By.XPATH, "..")

    # индикатор занятости
    busy_indicator = (By.XPATH, './/div[@class = "Modal_modal__P3_V5"]//div')
