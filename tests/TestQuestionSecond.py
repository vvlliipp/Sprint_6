from pages.PageQuestions import PageQuestions


class TestQuestionSecond:
    def test_question_second(self, driver):
        page_question = PageQuestions(driver)
        assert page_question.check_answer_displayed_correctly(1, 1,
        'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.')

