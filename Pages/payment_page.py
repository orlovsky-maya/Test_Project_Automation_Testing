import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *


class PaymentPage(BasePage):

    # Getting
    def get_finish_button(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (PaymentPageLocators.FINISH_BUTTON))

    # Actions

    def click_finish(self):
        self.get_finish_button().click()

    # Methods

    def payment(self):
        self.click_finish()