import pytest
from selenium import webdriver


@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.maximize_window()
    firefox.get("https://qa-scooter.praktikum-services.ru/")
    yield firefox
    firefox.quit()
