import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
# from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from pages.login_page import LoginPage
# from webdriver_manager.microsoft import EdgeDriverManager

# Parametrize the fixture to run tests in both Chrome and Firefox
# @pytest.fixture(params=["chrome", "firefox"])
# def browser(request):
#     if request.param == "chrome":
#         service = ChromeService(executable_path="/path/to/chromedriver")
#         driver = webdriver.Chrome(service=service)
#     elif request.param == "firefox":
#         service = FirefoxService(executable_path="/path/to/geckodriver")
#         driver = webdriver.Firefox(service=service)
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#     yield driver
#     driver.quit()

"""
This fixture is used to run tests in both Chrome and Firefox using command line, just pecify the browser when running pytest:
like pytest --browser chrome  pytest --browser firefox
This command will run the tests only in Chrome, as the fixture will check the --browser option and initialize only the specified browser.
"""
# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")

# @pytest.fixture(params=["chrome", "firefox"])
# def browser(request):
#     browser = request.config.getoption("--browser")
#     if browser == "chrome":
#         service = ChromeService(executable_path="/path/to/chromedriver")
#         driver = webdriver.Chrome(service=service)
#     elif browser == "firefox":
#         service = FirefoxService(executable_path="/path/to/geckodriver")
#         driver = webdriver.Firefox(service=service)
#     else:
#         raise ValueError(f"Unsupported browser: {browser}")
#     yield driver
#     driver.quit()
"""This fixture is used to run tests in both Chrome and Firefox using command line, just pecify the browser when running pytest:
like pytest --browser chrome  pytest --browser firefox
This command will run the tests only in Chrome, as the fixture will check the --browser option and initialize only the specified browser.
"""
def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests on")
@pytest.fixture(scope="session")
def browser(request):
    browser_name = request.config.getoption("--browser")
    if browser_name == "chrome":
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    # elif browser_name == "edge":
    #     driver = webdriver.Edge(service=EdgeService(EdgeDriverManager().install()))
    # elif browser_name == "safari" and platform.system() == 'Darwin':  # Safari is only available on macOS
    #     driver = webdriver.Safari()
    else:
        raise ValueError(f"Unsupported browser: {browser_name}")
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login_page(browser):
    browser.get("https://www.facebook.com/")
    return LoginPage(browser)
