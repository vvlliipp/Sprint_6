from locators.PageOrder import Order
from pages.base_page import BasePage
from locators.Metro_page import Metro


class PageOrder(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    def click_order_top_button(self):
        self.click_element(Order.order_top)

    def click_order_below_button(self):
        self.click_element(Order.order_below)

    def fill_order_form_one(self, name, surname, address, phone):
        self.fill_field(Order.name_field, name)
        self.fill_field(Order.surname_field, surname)
        self.fill_field(Order.address_field, address)
        self.fill_field(Order.phone_number_field, phone)

    def fill_metro_field(self):
        self.fill_field(Metro.metro_input, "Черкизовская")
        self.click_element(Metro.get_metro_station("Черкизовская"))

    def click_on_the_next_button(self):
        self.click_element(Order.button_further)

    def fill_order_form_two(self, comment):
        self.click_element(Order.date_field)
        self.click_element(Order.day)
        self.click_element(Order.rental_field)
        self.click_element(Order.rental_period)
        self.click_element(Order.black_pearl)
        self.fill_field(Order.comment_field, comment)

    def click_order_button(self):
        self.click_element(Order.button_order)

    def order_confirmation(self):
        self.click_element(Order.order_confirmation)
