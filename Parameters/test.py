from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import pytest
import time
import math


links = ["https://stepik.org/lesson/236895/step/1",
         "https://stepik.org/lesson/236896/step/1",
         "https://stepik.org/lesson/236897/step/1",
         "https://stepik.org/lesson/236898/step/1",
         "https://stepik.org/lesson/236899/step/1",
         "https://stepik.org/lesson/236903/step/1",
         "https://stepik.org/lesson/236904/step/1",
         "https://stepik.org/lesson/236905/step/1"]

totalName = " "


class TestMethodMainPage():

    @pytest.mark.parametrize('links, totalName', links, totalName)
    def test_guest_should_see_login_link(self,  browser, links, totalName):
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
        if (textr.text != "Correct!"):
            totalName += textr.text
        print(f"\n{totalName}")
