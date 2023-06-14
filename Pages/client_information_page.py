import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *
from Utilities.Logger import Logger


class ClientInformationPage(BasePage):

    # Getting
    def get_first_name(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (ClientInformationPageLocators.FIRST_NAME))

    def get_last_name(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (ClientInformationPageLocators.LAST_NAME))

    def get_postal_code(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (ClientInformationPageLocators.POSTAL_CODE))

    def get_continue_button(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable
                                                               (ClientInformationPageLocators.CONTINUE_BUTTON))

    # Actions

    def input_first_name(self, email):
        self.get_first_name().send_keys(email)

    def input_last_name(self, password):
        self.get_last_name().send_keys(password)

    def input_postal_code(self, password):
        self.get_postal_code().send_keys(password)

    def click_continue_button(self):
        self.get_continue_button().click()

    # Methods

    def input_information(self, first_name, last_name, postal_code):
        with allure.step('Input information'):
            Logger.add_start_step(method='input_information')
            self.input_first_name(first_name)
            self.input_last_name(last_name)
            self.input_postal_code(postal_code)
            self.click_continue_button()
            Logger.add_end_step(url=self.browser.current_url, method='input_information')