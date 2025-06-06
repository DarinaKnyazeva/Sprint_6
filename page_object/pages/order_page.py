import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from data import DZEN_PAGE
from page_object.locators.main_page_locators import MainPageLocators
from page_object.locators.order_page_locators import OrderPageLocators
from page_object.pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step('Заполнение первой части формы заказа')
    def set_order_first_part(self, data):
        self.element_click(OrderPageLocators.NAME_INPUT)
        self.add_text_to_element(OrderPageLocators.NAME_INPUT, data['name'])
        self.element_click(OrderPageLocators.SURNAME_INPUT)
        self.add_text_to_element(OrderPageLocators.SURNAME_INPUT, data['surname'])
        self.element_click(OrderPageLocators.ADDRESS_INPUT)
        self.add_text_to_element(OrderPageLocators.ADDRESS_INPUT, data['address'])
        self.element_click(OrderPageLocators.STATION_DROPDOWN_CLICK)
        self.element_click(OrderPageLocators.STATION_SELECT)
        self.element_click(OrderPageLocators.PHONE_INPUT)
        self.add_text_to_element(OrderPageLocators.PHONE_INPUT, data['phone'])
        self.element_click(OrderPageLocators.CONTINUE_BUTTON)

    @allure.step('Заполнение второй части формы заказа')
    def set_order_second_part(self, data):
        self.element_click(OrderPageLocators.DATE_INPUT)
        self.add_text_to_element(OrderPageLocators.DATE_INPUT, data['date'])
        self.element_click(OrderPageLocators.ROOT_LOCATOR)
        self.element_click(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.element_click(OrderPageLocators.RENTAL_PERIOD_SELECT)
        self.element_click(OrderPageLocators.ORDER_BUTTON_MID)
        self.element_click(OrderPageLocators.SUBMIT_BUTTON)

    @allure.step('Создание заказа')
    def create_order(self, data):
        self.set_order_first_part(data)
        self.set_order_second_part(data)

    @allure.step('Проверка заказа')
    def check_order(self, locator):
        return self.get_text_from_elm(locator)

    @allure.step('Проверка статуса заказа')
    def check_order_status(self):
        self.element_click(OrderPageLocators.ORDER_STATUS)

    @allure.step('Клик на лого Самоката')
    def click_to_logo(self):
        self.element_click(MainPageLocators.SCOOTER_LOGO)

    @allure.step('Клик на лого Яндекса')
    def click_to_yandex_logo(self):
        current_windows = self.driver.window_handles
        self.element_click(MainPageLocators.YANDEX_LOGO)

        WebDriverWait(self.driver, 10).until(
            lambda driver: len(driver.window_handles) > len(current_windows))

        new_window = [handle for handle in self.driver.window_handles
                      if handle not in current_windows][0]
        self.driver.switch_to.window(new_window)

        WebDriverWait(self.driver, 300).until(
            expected_conditions.url_contains(DZEN_PAGE))
