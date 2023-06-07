import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *


class FinishPage(BasePage):

    # Getting

    # Actions

    # Methods

    def finish(self):
        self.assert_url('https://www.saucedemo.com/checkout-complete.html')
        self.get_screenshot()