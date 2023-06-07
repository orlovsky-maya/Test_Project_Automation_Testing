import time
from selenium import webdriver
from Pages.main_page import MainPage
from Pages.login_page import LoginPage
from Pages.cart_page import CartPage
from Pages.client_information_page import ClientInformationPage
from Pages.payment_page import PaymentPage
from Pages.finish_page import FinishPage

# The syntax to run the script on Ubuntu OS
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_argument("--remote-debugging-port=9515")
browser = webdriver.Chrome(options=chrome_options)


link = 'https://www.saucedemo.com/'

# User credentials
user = 'standard_user'
password = 'secret_sauce'

# User information
first_name = "Maya"
last_name = "Orlovskaya"
postal_code = "12345"


def test_buy_product_1():
    lp = LoginPage(browser, link)
    lp.authorization(user, password)

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


def test_buy_product_2():
    lp = LoginPage(browser, link)
    lp.authorization(user, password)

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

