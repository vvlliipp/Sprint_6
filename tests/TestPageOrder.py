import pytest
from pages.PageOrder import PageOrder
from locators.PageOrder import Order
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.parametrize("color, is_top_button, expected_url", [
    ('чёрный жемчуг', True, 'https://qa-scooter.praktikum-services.ru/'),
    ('серая безысходность', False, 'dzen.ru'),
])
def test_order(driver, color, is_top_button, expected_url):
    page_order = PageOrder(driver)
    page_order.close_cookie()
    page_order.click_order_button(is_top_button)
    page_order.fill_order_form_one()
    page_order.fill_order_form_two(color=color)
    page_order.submit_order()

    try:
        WebDriverWait(driver, 20).until(
            expected_conditions.visibility_of_element_located(Order.view_status)
        )
        view_status_button = driver.find_element(*Order.view_status)
        assert view_status_button.text == 'Посмотреть статус', "Статус заказа не виден"
    except Exception as e:
        print(f"Ошибка при ожидании статуса заказа: {e}")


    if color == 'чёрный жемчуг':
        page_order.click_logo_scooter()
        WebDriverWait(driver, 30).until(
            expected_conditions.url_to_be(expected_url)
        )
        assert driver.current_url == expected_url, 'Не удалось вернуться на главную страницу Самоката'
    elif color == 'серая безысходность':
        page_order.click_logo_yandex()
        WebDriverWait(driver, 30).until(expected_conditions.number_of_windows_to_be(2))
        new_window = driver.window_handles[1]
        driver.switch_to.window(new_window)

        WebDriverWait(driver, 30).until(
            expected_conditions.url_contains('dzen.ru')
        )
        assert 'dzen.ru' in driver.current_url, 'Не открылся Дзен после нажатия на логотип Яндекса'
