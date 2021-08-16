from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math


links = ["https://stepik.org/lesson/236895/step/1"]


@pytest.fixture(scope="function")
def browser():
    print("\nstart browser for test..")
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    browser = webdriver.Chrome(options=options)
    yield browser
    print("\nquit browser..")
    # browser.quit()


class TestMethodMainPage():

    totalName = ""

    @pytest.mark.parametrize('links', links)
    def test_guest_should_see_login_link(self, browser, links):
        browser.get(links)
        answer = str(math.log(int(time.time())))
        area = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.TAG_NAME, "textarea")))
        area.send_keys(answer)
        button = WebDriverWait(browser, 10).until(
            EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission")))
        button.click()
        textr = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".smart-hints__hint")))
        print(textr.text())
        if textr != "Correct!":
            self.totalName += textr.text()
