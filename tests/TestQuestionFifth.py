from pages.PageQuestions import PageQuestions


class TestQuestionFifth:
    def test_question_fifth(self, driver):
        page_question = PageQuestions(driver)
        assert page_question.check_answer_displayed_correctly(4, 4,
        'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.')
