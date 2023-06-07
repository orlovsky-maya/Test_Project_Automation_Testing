from Pages.main_page import MainPage
from conftest import link


def test_link_about(browser, setup):
    mp = MainPage(browser, link)
    mp.select_menu_about()
    print('FINISH about link')


