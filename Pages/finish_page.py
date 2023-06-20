import allure
from Base.base_page import BasePage


class FinishPage(BasePage):

    # Getting

    # Actions

    # Methods

    def finish(self, directory):
        with allure.step('finish'):
            self.logger.add_start_step(method='finish')
            self.assert_url('https://www.saucedemo.com/checkout-complete.html')
            self.get_screenshot(directory)
            self.logger.add_end_step(url=self.browser.current_url, method='finish')