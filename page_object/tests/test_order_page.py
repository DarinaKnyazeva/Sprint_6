import allure
import pytest

from conftest import driver, main_page, order_page
from data import FIRST_ORDER_DATA, SECOND_ORDER_DATA, MAIN_PAGE_URL, DZEN_PAGE
from page_object.locators.main_page_locators import MainPageLocators


@allure.feature('Страница заказа самоката')
class TestOrderPage:

    @allure.title('Заказ самоката')
    @pytest.mark.parametrize(
        'locator, order_data',
        [(MainPageLocators.ORDER_BUTTON_UP, FIRST_ORDER_DATA),
         (MainPageLocators.ORDER_BUTTON_UP, SECOND_ORDER_DATA)
         ]
    )
    def test_create_order(self, main_page, order_page, locator, order_data):
        main_page.element_click(locator)
        order_page.create_order(order_data)
        assert order_page.check_order(locator)

    @allure.title('Проверка перехода по лого самоката на главную страницу')
    @pytest.mark.parametrize(
        'locator, order_data',
        [(MainPageLocators.ORDER_BUTTON_UP, FIRST_ORDER_DATA),
         (MainPageLocators.ORDER_BUTTON_UP, SECOND_ORDER_DATA)
         ]
    )
    def test_check_url(self, main_page, order_page, locator, order_data):
        main_page.element_click(locator)
        order_page.create_order(order_data)
        order_page.check_order_status()
        order_page.click_to_logo()
        assert order_page.get_current_url() == MAIN_PAGE_URL

    @allure.title('Проверка перехода по лого Яндекса на страницу Дзен')
    @pytest.mark.parametrize(
        'locator, order_data',
        [(MainPageLocators.ORDER_BUTTON_UP, FIRST_ORDER_DATA),
         (MainPageLocators.ORDER_BUTTON_UP, SECOND_ORDER_DATA)
         ]
    )
    def test_check_url_dzen(self, main_page, order_page, locator, order_data):
        main_page.element_click(locator)
        order_page.create_order(order_data)
        order_page.check_order_status()
        order_page.click_to_yandex_logo()
        assert DZEN_PAGE in order_page.get_current_url()
