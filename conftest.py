import allure
import pytest
from selenium import webdriver
from Pages.login_page import LoginPage
from Utilities.Logger import Logger

link = 'https://www.saucedemo.com/'

# User credentials
user = 'standard_user'
password = 'secret_sauce'


@pytest.fixture(scope="function")
def browser():
    print("\nstart firefox browser for test..")
    firefox_options = webdriver.FirefoxOptions()
    browser = webdriver.Remote(
        command_executor='http://firefox_grid:4444',
        options=firefox_options
    )

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
