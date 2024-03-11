import pytest
from pages.login_page import LoginPage
from utils.read_data import read_json_data as read_json_data

# @pytest.mark.parametrize("testdata", read_csv_data("/Users/arunbasil/PycharmProjects/pythonFacebookAutomation/data/test_data.csv"))
@pytest.mark.parametrize("testdata", read_json_data("/Users/arunbasil/PycharmProjects/pythonFacebookAutomation/data/test_data.json"))
def test_facebook_login(testdata, browser):
    login_page = LoginPage(browser)
    # browser.get("https://www.facebook.com/")
    login_page.navigate_to_url()
    login_page.enter_username(testdata['username'])
    login_page.enter_password(testdata['password'])
    login_page.click_login_button()
    # Further assertions based on the scenario
