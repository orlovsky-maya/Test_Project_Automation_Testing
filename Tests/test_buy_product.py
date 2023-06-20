import allure
from Pages.main_page import MainPage
from Pages.cart_page import CartPage
from Pages.client_information_page import ClientInformationPage
from Pages.payment_page import PaymentPage
from Pages.finish_page import FinishPage
from conftest import link

# User information
first_name = "Maya"
last_name = "Orlovskaya"
postal_code = "12345"


@allure.description('Test buy product 1')
def test_buy_product_1(browser, setup, request, logger):
    mp = MainPage(browser, link, logger)
    mp.select_product_1()

    cp = CartPage(browser, link, logger)
    cp.product_confirmation()

    cip = ClientInformationPage(browser, link, logger)
    cip.input_information(first_name, last_name, postal_code)

    pp = PaymentPage(browser, link, logger)
    pp.payment()

    f = FinishPage(browser, link, logger)
    f.finish(request.config.rootdir)


@allure.description('Test buy product 2')
def test_buy_product_2(browser, setup, request, logger):
    mp = MainPage(browser, link, logger)
    mp.select_product_2()

    cp = CartPage(browser, link, logger)
    cp.product_confirmation()

    cip = ClientInformationPage(browser, link, logger)
    cip.input_information(first_name, last_name, postal_code)

    pp = PaymentPage(browser, link, logger)
    pp.payment()

    f = FinishPage(browser, link, logger)
    f.finish(request.config.rootdir)
