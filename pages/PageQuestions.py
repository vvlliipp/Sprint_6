from locators.PageQuestions import Questions
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class PageQuestions:
    def __init__(self, driver):
        self.driver = driver

    def scroll_to_element(self, element):
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def click_question(self, question_number):
        questions = [
                Questions.first_question, Questions.second_question, Questions.third_question,
                Questions.fourth_question, Questions.fifth_question, Questions.sixth_question,
                Questions.seventh_question, Questions.eighth_question
            ]

        question_element = WebDriverWait(self.driver, 10).until(
            expected_conditions.visibility_of_element_located(questions[question_number])
        )

        self.scroll_to_element(question_element)

        WebDriverWait(self.driver, 10).until(
            expected_conditions.element_to_be_clickable(questions[question_number])
        )

        question_element.click()

    def get_answer(self, answer_number):
        answers = [
            Questions.first_answer, Questions.second_answer, Questions.third_answer,
            Questions.fourth_answer, Questions.fifth_answer, Questions.sixth_answer,
            Questions.seventh_answer, Questions.eighth_answer
        ]
        return self.driver.find_element(*answers[answer_number]).text

    def check_answer_displayed_correctly(self, question_number, answer_number, expected_text):
        self.click_question(question_number)
        actual_text = self.get_answer(answer_number)
        return actual_text == expected_text
