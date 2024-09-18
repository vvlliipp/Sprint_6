from pages.PageQuestions import PageQuestions


class TestQuestionEighth:
    def test_question_eighth(self, driver):
        page_question = PageQuestions(driver)
        assert page_question.check_answer_displayed_correctly(7, 7,
        'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
