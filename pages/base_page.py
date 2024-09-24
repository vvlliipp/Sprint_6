from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.remote.webdriver import WebDriver
from locators.PageOrder import Order


class BasePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def open_page(self, url):
        self.driver.get(url)

    def click_cookies(self):
        self.wait_and_find_element(Order.cookie).click()

    def get_element_text(self, locator):
        element = WebDriverWait(self.driver, 10).until(expected_conditions.presence_of_element_located(locator))
        return element.text

    def scroll_to_element(self, locator):
        element = self.wait_and_find_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def click_element(self, locator):
        element = self.wait_and_find_element(locator)
        element.click()

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
