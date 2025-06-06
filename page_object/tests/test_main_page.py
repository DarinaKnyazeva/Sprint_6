import allure
import pytest

from data import ANSWER_DATA
from conftest import main_page, driver


class TestMainPage:

    # @allure.title('Проверка списка вопросов и ответов')
    @pytest.mark.parametrize(
        "num", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_qa(self, main_page, num):
        assert main_page.check_qa(num) == ANSWER_DATA[num]
