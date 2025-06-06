from selenium.webdriver.common.by import By


class MainPageLocators:
    QUESTION_LOCATOR = By.XPATH, './/*[@id="accordion__heading-{}"]'
    ANSWER_LOCATOR = By.XPATH, './/*[@id="accordion__panel-{}"]'
    QUESTION_TO_SCROLL_LOCATOR = By.XPATH, './/*[@id="accordion__heading-7"]'
    ORDER_BUTTON_UP = By.XPATH, '.// *[@class="Button_Button__ra12g"]'
    ORDER_BUTTON_MID = By.XPATH, '.// *[@class="Button_Button__ra12g Button_Middle__1CSJM"]'
    SCOOTER_LOGO = By.XPATH, './/*[@alt="Scooter"]'
    YANDEX_LOGO = By.XPATH, './/*[@href="//yandex.ru"]'



