from locators.PageOrder import Order
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.Metro_page import Metro
from data import Data


class PageOrder:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView(true);", element)

    def close_cookie(self):
        try:
            cookie_close_button = WebDriverWait(self.driver, 20).until(
                expected_conditions.element_to_be_clickable(Order.cookie))
            cookie_close_button.click()
        except Exception as e:
            print(f"Сообщение о cookie не найдено или не удалось закрыть: {e}")

    def click_order_button(self, is_top_button=True):
        self.close_cookie()
        button = Order.order_top if is_top_button else Order.order_below
        button_element = self.driver.find_element(*button)
        self.scroll_to_element(button_element)
        WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable(button_element)).click()

    def fill_order_form_one(self):
        first_form_data = Data.data_of_the_first_form()

        WebDriverWait(self.driver, 20).until(
            expected_conditions.presence_of_element_located(Order.name_field)).send_keys(first_form_data["name"])
        self.driver.find_element(*Order.surname_field).send_keys(first_form_data["surname"])
        self.driver.find_element(*Order.address_field).send_keys(first_form_data["address"])

        metro_field = "Черкизовская"
        self.driver.find_element(*Metro.metro_input).send_keys(metro_field)
        self.driver.find_element(*Metro.get_metro_station(metro_field)).click()

        self.driver.find_element(*Order.phone_number_field).send_keys(first_form_data["phone"])

        self.driver.find_element(*Order.button_further).click()

    def fill_order_form_two(self, color):
        self.driver.find_element(*Order.date_field).click()
        self.driver.find_element(*Order.day).click()

        self.driver.find_element(*Order.rental_field).click()
        self.driver.find_element(*Order.rental_period).click()

        self.select_scooter_color(color)

        self.driver.find_element(*Order.comment_field).send_keys("Спасибо")

    def select_scooter_color(self, color):
        if color.lower() == 'чёрный жемчуг':
            self.driver.find_element(*Order.black_pearl).click()
        elif color.lower() == 'серая безысходность':
            self.driver.find_element(*Order.gray_hopelessness).click()

    def submit_order(self):
        self.driver.find_element(*Order.button_order).click()
        self.driver.find_element(*Order.order_confirmation).click()
        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(Order.view_status)).click()

    def click_logo_scooter(self):
        WebDriverWait(self.driver, 15).until(
            expected_conditions.visibility_of_element_located(Order.logo_scooter)).click()

    def click_logo_yandex(self):
        self.driver.find_element(*Order.logo_yandex).click()
        WebDriverWait(self.driver, 20).until(expected_conditions.number_of_windows_to_be(2))
        new_window = self.driver.window_handles[1]
        self.driver.switch_to.window(new_window)
        return self.driver.current_url
