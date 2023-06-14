import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *
from Utilities.Logger import Logger


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
        with allure.step('Product confirmation'):
            Logger.add_start_step(method='product_confirmation')
            self.get_checkout_button()
            self.click_checkout()
            Logger.add_end_step(url=self.browser.current_url, method='product_confirmation')