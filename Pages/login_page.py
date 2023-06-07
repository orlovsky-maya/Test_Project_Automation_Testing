from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Base.base_page import BasePage
from Base.locators import *


class LoginPage(BasePage):

    # Getting
    def get_user_name(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable(LoginPageLocators.USER_NAME))

    def get_user_password(self):
        return WebDriverWait(self.browser, self.timeout).until(EC.element_to_be_clickable(LoginPageLocators.PASSWORD))

    def get_login_button(self):
        return WebDriverWait(self.browser, self.timeout).until(
            EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON))

    def get_main_word(self):
        return WebDriverWait(self.browser, self.timeout).until(
            EC.visibility_of_element_located(ProductsPageLocators.PRODUCT_HEADER))

    # Actions

    def input_user_name(self, email):
        self.get_user_name().send_keys(email)

    def input_password(self, password):
        self.get_user_password().send_keys(password)

    def click_login_button(self):
        self.get_login_button().click()

    # Methods

    def authorization(self, login_name, login_password):
        self.open()
        self.input_user_name(login_name)
        self.input_password(login_password)
        self.click_login_button()
        self.assert_word(self.get_main_word(), "Products")