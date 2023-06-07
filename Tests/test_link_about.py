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


def test_link_about():
    lp = LoginPage(browser, link)
    lp.authorization(user, password)

    mp = MainPage(browser, link)
    mp.select_menu_about()

    print('FINISH')
    browser.quit()


