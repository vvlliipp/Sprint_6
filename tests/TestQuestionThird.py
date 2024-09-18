from pages.PageQuestions import PageQuestions


class TestQuestionThird:
    def test_question_third(self, driver):
        page_question = PageQuestions(driver)
        assert page_question.check_answer_displayed_correctly(2, 2,
        'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.')
