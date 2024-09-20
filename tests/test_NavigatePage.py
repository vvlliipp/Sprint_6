import pytest
from pages.page_Questions import PageQuestions
from data import Url


class TestLogoRedirect:
    def test_scooter_logo_redirect(self, driver):
        page = PageQuestions(driver)
        page.click_logo_scooter()
        assert page.check_title_scooter()

    def test_yandex_logo_redirect(self, driver):
        page = PageQuestions(driver)
        page.click_logo_yandex()
        url = page.wait_url_contains(Url.PAGE_DZEN)
        assert Url.PAGE_DZEN in url
