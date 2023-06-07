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


def test_buy_product_1(browser, setup):
    mp = MainPage(browser, link)
    mp.select_product_1()

    cp = CartPage(browser, link)
    cp.product_confirmation()

    cip = ClientInformationPage(browser, link)
    cip.input_information(first_name, last_name, postal_code)

    pp = PaymentPage(browser, link)
    pp.payment()

    f = FinishPage(browser, link)
    f.finish()
    print('FINISH_1')


def test_buy_product_2(browser, setup):
    mp = MainPage(browser, link)
    mp.select_product_2()

    cp = CartPage(browser, link)
    cp.product_confirmation()

    cip = ClientInformationPage(browser, link)
    cip.input_information(first_name, last_name, postal_code)

    pp = PaymentPage(browser, link)
    pp.payment()

    f = FinishPage(browser, link)
    f.finish()
    print('FINISH_2')

