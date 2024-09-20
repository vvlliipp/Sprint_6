import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.common.exceptions import TimeoutException
from locators.PageOrder import Order


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def click_cookies(self):
        self.wait_and_find_element(Order.cookie).click()

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def find_element(self, locator: tuple[str, str], timeout: int = 10):
        try:
            return WebDriverWait(self.driver, timeout).until(expected_conditions.presence_of_element_located(locator))
        except TimeoutException:
            print(f"Element with locator {locator} not found within {timeout} seconds.")
            return None

    def click_element(self, locator: tuple[str, str], timeout: int = 10):
        element = self.find_element(locator, timeout)
        if element:
            element.click()
        else:
            pytest.fail(f"Failed to click on element with locator {locator}.")

    def wait_and_find_element(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        return self.driver.find_element(*locator)

    def fill_field(self, locator, data):
        element = self.wait_and_find_element(locator)
        element.send_keys(data)

    def get_page_title(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        return self.driver.title

    def check_element_display(self, locator):
        return self.driver.find_element(*locator).is_displayed()

    def wait_url_contains(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_contains(url))
        return self.driver.current_url

    def switch_to_last_window(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def wait_for_url(self, url):
        self.switch_to_last_window()
        url = self.wait_url_contains(url)
        return url
