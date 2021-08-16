from os import link
from _pytest.assertion import pytest_sessionfinish
import py
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture(scope="function")
def browser():
    print("\n Start browser")
    browser = webdriver.Chrome()
    yield browser
    print("\n Close browser")
    browser.quit()


class TestMainPage():

    @pytest.mark.smoke
    def test_show_main_page(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")

    @pytest.mark.regression
    def test_main_page_has_button_authorisation(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector(".basket-mini .btn-group > a")
