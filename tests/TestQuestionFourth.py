from pages.PageQuestions import PageQuestions


class TestQuestionFourth:
    def test_question_fourth(self, driver):
        page_question = PageQuestions(driver)
        assert page_question.check_answer_displayed_correctly(3, 3,
        'Только начиная с завтрашнего дня. Но скоро станем расторопнее.')
