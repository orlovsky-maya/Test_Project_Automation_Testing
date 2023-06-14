from Base.base_page import BasePage
from Utilities.Logger import Logger
import allure


class FinishPage(BasePage):

    # Getting

    # Actions

    # Methods

    def finish(self):
        with allure.step('finish'):
            Logger.add_start_step(method='finish')
            self.assert_url('https://www.saucedemo.com/checkout-complete.html')
            self.get_screenshot()
            Logger.add_end_step(url=self.browser.current_url, method='finish')