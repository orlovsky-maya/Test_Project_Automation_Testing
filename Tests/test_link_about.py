import allure
from Pages.main_page import MainPage
from conftest import link


@allure.description('Test link about')
def test_link_about(browser, setup, logger):
    mp = MainPage(browser, link, logger)
    mp.select_menu_about()