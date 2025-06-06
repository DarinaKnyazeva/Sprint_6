import allure

from page_object.locators.main_page_locators import MainPageLocators
from page_object.pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Клик по вопросу')
    def click_to_question(self, num):
        formatter_locator = self.formed_locator(MainPageLocators.QUESTION_LOCATOR, num)
        self.scroll_to_elm(MainPageLocators.QUESTION_TO_SCROLL_LOCATOR)
        self.element_click(formatter_locator)

    @allure.step('Получение ответа на вопрос')
    def get_answer_text(self, num):
        formatter_locator = self.formed_locator(MainPageLocators.ANSWER_LOCATOR, num)
        return self.get_text_from_elm(formatter_locator)

    @allure.step('Проверка вопроса и ответа')
    def check_qa(self, num):
        self.click_to_question(num)
        return self.get_answer_text(num)
