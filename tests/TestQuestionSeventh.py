from pages.PageQuestions import PageQuestions


class TestQuestionSeventh:
    def test_question_seventh(self, driver):
        page_question = PageQuestions(driver)
        assert page_question.check_answer_displayed_correctly(6, 6,
        'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.')
