from selenium.webdriver.common.by import By


class OrderPageLocators:
    NAME_INPUT = By.XPATH, './/*[@placeholder="* Имя"]'
    SURNAME_INPUT = By.XPATH, './/*[@placeholder="* Фамилия"]'
    ADDRESS_INPUT = By.XPATH, './/*[@placeholder="* Адрес: куда привезти заказ"]'
    STATION_DROPDOWN_CLICK = By.XPATH, './/div[@class="select-search"]/div[@class="select-search__value"]'
    STATION_SELECT = By.XPATH, './/*[@class="Order_Text__2broi" and text()="Черкизовская"]'
    PHONE_INPUT = By.XPATH, './/*[@placeholder="* Телефон: на него позвонит курьер"]'
    CONTINUE_BUTTON = By.XPATH, './/*[text()="Далее"]'
    DATE_INPUT = By.XPATH, './/*[@placeholder="* Когда привезти самокат"]'
    RENTAL_PERIOD_DROPDOWN = By.XPATH, '.// *[@class="Dropdown-control"]'
    RENTAL_PERIOD_SELECT = By.XPATH, '.// *[@class="Dropdown-option" and text()="сутки"]'
    ORDER_BUTTON_MID = By.XPATH, '.// *[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    SUBMIT_BUTTON = By.XPATH, './/*[text()="Да"]'
    ROOT_LOCATOR = By.XPATH, './/*[@id="root"]'
    SUBMIT_ORDER_MESSAGE = By.XPATH, './/*[text()="Заказ оформлен"]'
    ORDER_STATUS = By.XPATH, './/*[text()="Посмотреть статус"]'
