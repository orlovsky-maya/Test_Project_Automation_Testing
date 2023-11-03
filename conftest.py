import allure
import pytest
from selenium import webdriver
from Pages.login_page import LoginPage
from Utilities.Logger import Logger
from selenium.webdriver.chrome.options import Options

link = 'https://www.saucedemo.com/'

# User credentials
user = 'standard_user'
password = 'secret_sauce'


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")
    parser.addoption('--run_tests', action='store', default=None,
                     help="Choose run method: docker or local")


@pytest.fixture(scope="function")
def browser(request):
    browser_name = request.config.getoption("browser_name")
    run_tests = request.config.getoption("run_tests")

    if run_tests == "docker":
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
    elif run_tests == "local":
        if browser_name == "chrome":
            print("\nstart chrome browser for test..")
            chrome_options = Options()
            chrome_options.add_argument("--remote-debugging-port=9515")
            browser = webdriver.Chrome(options=chrome_options)
        elif browser_name == "firefox":
            print("\nstart firefox browser for test..")
            fp = webdriver.FirefoxProfile()
            browser = webdriver.Firefox(firefox_profile=fp)
        else:
            raise pytest.UsageError("--browser_name should be chrome or firefox")
        yield browser
        print("\nquit browser..")
        browser.quit()
    else:
        raise pytest.UsageError("--run_tests should be docker or local")

@pytest.fixture(scope="function", autouse=True)
def setup(browser, logger):
    with allure.step('setup'):
        lp = LoginPage(browser, link, logger)
        lp.authorization(user, password)


@pytest.fixture()
def logger(request):
    logger = Logger(request.config.rootdir)
    return logger
