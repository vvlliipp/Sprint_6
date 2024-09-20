from selenium.webdriver.common.by import By


class Questions:
    first_question = By.ID, "accordion__heading-0"
    second_question = By.ID, "accordion__heading-1"
    third_question = By.ID, "accordion__heading-2"
    fourth_question = By.ID, "accordion__heading-3"
    fifth_question = By.ID, "accordion__heading-4"
    sixth_question = By.ID, "accordion__heading-5"
    seventh_question = By.ID, "accordion__heading-6"
    eighth_question = By.ID, "accordion__heading-7"
    first_answer = By.ID, "accordion__panel-0"
    second_answer = By.ID, "accordion__panel-1"
    third_answer = By.ID, "accordion__panel-2"
    fourth_answer = By.ID, "accordion__panel-3"
    fifth_answer = By.ID, "accordion__panel-4"
    sixth_answer = By.ID, "accordion__panel-5"
    seventh_answer = By.ID, "accordion__panel-6"
    eighth_answer = By.ID, "accordion__panel-7"
    logo_scooter = By.XPATH, "//*[@class='Header_LogoScooter__3lsAR']"
    logo_yandex = By.XPATH, "//*[@class='Header_LogoYandex__3TSOI']"
    title_scooter = By.XPATH, "//div[contains(@class, 'Home_Header')]"
    list_of_question = By.CLASS_NAME, "accordion"
