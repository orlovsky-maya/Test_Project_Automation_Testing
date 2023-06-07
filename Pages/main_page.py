import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *


class MainPage(BasePage):

    # Getting
    def get_product_1(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (ProductsPageLocators.PRODUCT_1))

    def get_product_2(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (ProductsPageLocators.PRODUCT_2))

    def get_cart(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (ProductsPageLocators.CART_BUTTON))

    def get_menu(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (ProductsPageLocators.MENU))

    def get_link_about(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (ProductsPageLocators.ABOUT_LINK))

    # Actions
    def click_select_product_1(self):
        self.get_product_1().click()

    def click_select_product_2(self):
        self.get_product_2().click()

    def click_cart(self):
        self.get_cart().click()

    def click_menu(self):
        self.get_menu().click()

    def click_link_about(self):
        self.get_link_about().click()

    # Methods

    def select_product_1(self):
        self.click_select_product_1()
        self.click_cart()

    def select_product_2(self):
        self.click_select_product_2()
        self.click_cart()

    def select_menu_about(self):
        self.click_menu()
        self.click_link_about()
        self.assert_url('https://saucelabs.com/')