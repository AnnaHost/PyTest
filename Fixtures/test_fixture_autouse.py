import pytest
from selenium import webdriver


link = "http://selenium1py.pythonanywhere.com/"


@pytest.fixture
def browser(scope="class"):
    print("\n Instant browser for test")
    browser = webdriver.Chrome()
    yield browser
    print("\n quit browser")
    browser.quit()


@pytest.fixture(autouse=True)
def prepare_data():
    print("\npreparing some critical data for every test")


class Test_Main_Page_PS():
    def test_is_main_button_active(self, browser):
        browser.get(link)
        browser.find_element_by_css_selector("#login_link")
