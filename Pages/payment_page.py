import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *
from Utilities.Logger import Logger


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
        with allure.step('payment'):
            Logger.add_start_step(method='payment')
            self.click_finish()
            Logger.add_end_step(url=self.browser.current_url, method='payment')