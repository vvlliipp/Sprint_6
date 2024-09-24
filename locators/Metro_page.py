from selenium.webdriver.common.by import By


class Metro:
    metro_input = By.XPATH, "//input[@class = 'select-search__input']"

    @staticmethod
    def get_metro_station(metro_field):
        return By.XPATH, f"//*[@class = 'select-search__select']//*[text() = '{metro_field}']"
