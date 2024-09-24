from selenium.webdriver.common.by import By


class Order:
    cookie = By.XPATH, "//button[contains(@class, 'App_CookieButton__3cvqF') and text()='да все привыкли']"
    order_top = By.XPATH, "//button[@class = 'Button_Button__ra12g']"
    order_below = By.XPATH, "//button[contains(@class, 'Button_Button') and text()='Заказать']"
    name_field = By.XPATH, "//input[@placeholder='* Имя']"
    surname_field = By.XPATH, "//input[@placeholder='* Фамилия']"
    address_field = By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']"
    phone_number_field = By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']"
    button_further = By.XPATH, "//button[text() = 'Далее']"
    date_field = By.XPATH, "//input[@placeholder='* Когда привезти самокат']"
    day = By.XPATH, "//div[contains(@class, 'react-datepicker__day') and contains(@aria-label, '4-е октября 2024 г.')]"
    rental_field = By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and text()='* Срок аренды']"
    rental_period = By.XPATH, "//div[@class='Dropdown-option' and text()='сутки']"
    black_pearl = By.XPATH, "//input[@id='black']"
    comment_field = By.XPATH, "//input[@placeholder='Комментарий для курьера']"
    button_order = By.XPATH, ".//div[3]/button[2]"
    order_confirmation = By.XPATH, "//button[text() = 'Да']"
    view_status = By.XPATH, "//button[text()='Посмотреть статус']"

