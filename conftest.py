import allure
import pytest
from selenium import webdriver
from Pages.login_page import LoginPage
from Utilities.Logger import Logger

link = 'https://www.saucedemo.com/'

# User credentials
user = 'standard_user'
password = 'secret_sauce'


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")

    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        chrome_options = webdriver.ChromeOptions()
        browser = webdriver.Remote(
            command_executor='http://chrome_grid:4444',
            options=chrome_options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        firefox_options = webdriver.FirefoxOptions()
        browser = webdriver.Remote(
            command_executor='http://firefox_grid:4444',
            options=firefox_options)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield browser
    print("\nquit browser..")
    browser.quit()


@pytest.fixture(scope="function", autouse=True)
def setup(browser, logger):
    with allure.step('setup'):
        lp = LoginPage(browser, link, logger)
        lp.authorization(user, password)


@pytest.fixture()
def logger(request):
    logger = Logger(request.config.rootdir)
    return logger
