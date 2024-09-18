from pages.PageQuestions import PageQuestions


class TestQuestionSixth:
    def test_question_sixth(self, driver):
        page_question = PageQuestions(driver)
        assert page_question.check_answer_displayed_correctly (5, 5,
        'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.')
