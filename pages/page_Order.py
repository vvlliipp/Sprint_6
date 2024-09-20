from locators.PageOrder import Order
from pages.base_page import BasePage
from locators.Metro_page import Metro


class PageOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_order_top_button(self):
        self.wait_and_find_element(Order.order_top)
        self.click_element(Order.order_top)

    def click_order_below_button(self):
        self.click_element(Order.order_below)

    def fill_order_form_one(self, name, surname, address, phone):
        self.wait_and_find_element(Order.name_field)
        self.fill_field(Order.name_field, name)

        self.wait_and_find_element(Order.surname_field)
        self.fill_field(Order.surname_field, surname)

        self.wait_and_find_element(Order.address_field)
        self.fill_field(Order.address_field, address)

        self.wait_and_find_element(Order.phone_number_field)
        self.fill_field(Order.phone_number_field, phone)

    def fill_metro_field(self):
        metro_field = "Черкизовская"
        self.driver.find_element(*Metro.metro_input).send_keys(metro_field)
        self.driver.find_element(*Metro.get_metro_station(metro_field)).click()

    def click_on_the_next_button(self):
        self.wait_and_find_element(Order.button_further)
        self.click_element(Order.button_further)

    def fill_order_form_two(self, comment):
        self.wait_and_find_element(Order.date_field)
        self.click_element(Order.date_field)
        self.click_element(Order.day)

        self.wait_and_find_element(Order.rental_field)
        self.click_element(Order.rental_field)
        self.click_element(Order.rental_period)

        self.click_element(Order.black_pearl)

        self.fill_field(Order.comment_field, comment)

    def click_order_button(self):
        self.click_element(Order.button_order)

    def order_confirmation(self):
        self.wait_and_find_element(Order.order_confirmation)
        self.click_element(Order.order_confirmation)

    def view_status(self):
        self.wait_and_find_element(Order.view_status)

