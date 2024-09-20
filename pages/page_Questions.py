from locators.PageQuestions import Questions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from pages.base_page import BasePage
from data import Url


class PageQuestions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def scroll_to_list_question(self):
        element = self.find_element(Questions.list_of_question)
        self.scroll_to_element(element)
        self.wait_and_find_element(Questions.list_of_question)

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        return element.text

    def check_element_text(self, locator, expected_text):
        actual_text = self.get_element_text(locator)
        assert actual_text == expected_text

    def click_logo_scooter(self):
        self.click_element(Questions.logo_scooter)
        WebDriverWait(self.driver, 10).until(
            expected_conditions.url_to_be(Url.PAGE_SCOOTER)
        )
        assert self.driver.current_url == 'https://qa-scooter.praktikum-services.ru/'

    def click_logo_yandex(self):
        self.driver.find_element(*Questions.logo_yandex).click()
        WebDriverWait(self.driver, 20).until(expected_conditions.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        return self.driver.current_url

    def check_title_scooter(self):
        return self.check_element_display(Questions.title_scooter)
