import pytest
from pages.page_Order import PageOrder
from data import Data
from locators.PageOrder import Order


def test_order_scooter_flow(driver):
    page_order = PageOrder(driver)

    page_order.click_cookies()
    page_order.click_order_top_button()

    page_order.fill_metro_field()
    page_order.fill_order_form_one(Data.NAME, Data.SURNAME, Data.ADDRESS, Data.PHONE)

    page_order.click_on_the_next_button()
    page_order.fill_order_form_two(Data.COMMENT)
    page_order.click_order_button()
    page_order.order_confirmation()

    view_status_button = driver.find_element(*Order.view_status)
    assert view_status_button.text == 'Посмотреть статус'
    view_status_button.click()

    page_order.click_order_below_button()

    page_order.fill_metro_field()
    page_order.fill_order_form_one(Data.NAME_2, Data.SURNAME_2, Data.ADDRESS_2, Data.PHONE_2)
    page_order.click_on_the_next_button()
    page_order.fill_order_form_two(Data.COMMENT_2)
    page_order.click_order_button()
    page_order.order_confirmation()

    view_status_button = driver.find_element(*Order.view_status)
    assert view_status_button.text == 'Посмотреть статус'
    view_status_button.click()

