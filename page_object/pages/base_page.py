import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    @allure.step('Инициализация браузера')
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Переход по URL')
    def go_to_url(self, url):
        self.driver.get(url)

    @allure.step('Поиск элемента с ожиданием')
    def find_elm_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик по элементу с ожиданием')
    def element_click(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))
        self.driver.find_element(*locator).click()

    @allure.step('Получение текста из элемента')
    def get_text_from_elm(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator).text

    @allure.step('Форматирование локатора')
    def formed_locator(self, num_locator, num):
        method, locator = num_locator
        locator = locator.format(num)
        return method, locator

    @allure.step('Скролл к элементу')
    def scroll_to_elm(self, locator):
        elm = self.driver.find_element(*locator)
        elm.is_enabled()
        self.driver.execute_script("arguments[0].scrollIntoView(true);", elm)

    @allure.step('Добавление текста в элемент')
    def add_text_to_element(self, locator, text):
        self.find_elm_with_wait(locator).send_keys(text)
