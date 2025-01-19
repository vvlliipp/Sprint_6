from locators.PageQuestions import Questions
from pages.base_page import BasePage
from data import Url


class PageQuestions(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def check_element_text(self, locator, expected_text):
        actual_text = self.get_element_text(locator)
        assert actual_text == expected_text

    def click_logo_scooter(self):
        self.click_element(Questions.logo_scooter)
        assert self.wait_for_url(Url.PAGE_SCOOTER) == Url.PAGE_SCOOTER

    def click_logo_yandex(self):
        self.click_element(Questions.logo_yandex)
        return self.wait_for_url(Url.PAGE_DZEN)

    def check_title_scooter(self):
        return self.check_element_display(Questions.title_scooter)
