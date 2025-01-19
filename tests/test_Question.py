import pytest
from data import Answer, Url
from locators.PageQuestions import Questions
from pages.page_Questions import PageQuestions


class TestQuestion:
    @pytest.mark.parametrize('question, answer, expected_answer',
    [
        [Questions.first_question, Questions.first_answer, Answer.ANSWER_1],
        [Questions.second_question, Questions.second_answer, Answer.ANSWER_2],
        [Questions.third_question, Questions.third_answer, Answer.ANSWER_3],
        [Questions.fourth_question, Questions.fourth_answer, Answer.ANSWER_4],
        [Questions.fifth_question, Questions.fifth_answer, Answer.ANSWER_5],
        [Questions.sixth_question, Questions.sixth_answer, Answer.ANSWER_6],
        [Questions.seventh_question, Questions.seventh_answer, Answer.ANSWER_7],
        [Questions.eighth_question, Questions.eighth_answer, Answer.ANSWER_8]
    ])
    def test_check_question_answer(self, driver, question, answer, expected_answer):
        page = PageQuestions(driver)
        page.open_page(Url.PAGE_SCOOTER)
        page.click_cookies()
        page.scroll_to_element(Questions.list_of_question)
        page.click_element(question)
        actual_answer = page.get_element_text(answer)
        assert actual_answer == expected_answer
