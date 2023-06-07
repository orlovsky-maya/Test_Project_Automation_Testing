import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *


class MainPage(BasePage):

    # Getting
    def get_product_1(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable(ProductsPageLocators.PRODUCT_1))

    def get_cart(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable(ProductsPageLocators.CART_BUTTON))

    # Actions
    def select_product_1(self):
        self.get_product_1().click()

    def click_cart(self):
        self.get_cart().click()

    # Methods

    def select_product(self):
        self.select_product_1()
        self.click_cart()