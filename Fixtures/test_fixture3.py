from _pytest.config.exceptions import PrintHelp
import pytest
from selenium import webdriver

link = "http://selenium1py.pythonanywhere.com/"


def test_guest_should_see_login_link(browser):
    browser.find_element_by_css_selector("#login_link")
    print("123")


def test_guest_should_see_basket_link_on_the_main_page():
    print("1232")
