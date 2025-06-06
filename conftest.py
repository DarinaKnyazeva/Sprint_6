import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from data import MAIN_PAGE_URL
from page_object.pages.main_page import MainPage
from page_object.pages.order_page import OrderPage


@pytest.fixture(params=["firefox"])
def driver(request):
    driver_instance = webdriver.Firefox()
    yield driver_instance
    driver_instance.quit()


@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    page.go_to_url(MAIN_PAGE_URL)
    return page


@pytest.fixture
def order_page(driver):
    page = OrderPage(driver)
    page.go_to_url(MAIN_PAGE_URL)
    return page
