from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *


class CartPage(BasePage):

    # Getting
    def get_checkout_button(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (CartPageLocators.CHECKOUT_BUTTON))

    # Actions

    def click_checkout(self):
        self.get_checkout_button().click()

    # Methods

    def product_confirmation(self):
        self.get_checkout_button()
        self.click_checkout()