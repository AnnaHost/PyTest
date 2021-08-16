from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    browser.implicitly_wait(7)
    yield browser
    print("\nquit browser..")
    browser.quit()


class TestMethodMainPage():

    @pytest.mark.parametrize('links', links)
    def test_guest_should_see_login_link(self, browser, links):
        browser.get(links)
        browser.find_element_by_tag_name("textarea").send_keys(str(answer))
        button = WebDriverWait(browser, 7).until(
            EC.element_to_be_clickable(By.CLASS_NAME, ("submit-submission")))
        textr = WebDriverWait(browser, 7).until(
            EC.visibility_of_element_located(By.ID, "ember169"), "Correct").text()
        print(textr)
