from pages.PageQuestions import PageQuestions


class TestQuestionFirst:
    def test_question_first(self, driver):
        page_questions = PageQuestions(driver)
        assert page_questions.check_answer_displayed_correctly(0,0,
            'Сутки — 400 рублей. Оплата курьеру — наличными или картой.')
