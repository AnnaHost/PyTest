from selenium import webdriver
import pytest
import time
import math


answer = math.log(int(time.time()))

links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    browser.implicity_wait(7)
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.mark.parametrize('links', links)
def test_guest_should_see_login_link(browser, links):
    browser.get(links)
    browser.find_element_by_taf_name("textarea").send_keys(str(answer))
