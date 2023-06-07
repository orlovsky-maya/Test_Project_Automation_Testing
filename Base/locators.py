from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER_NAME = (By.ID, 'user-name')
    PASSWORD = (By.ID, 'password')
    LOGIN_BUTTON = (By.ID, 'login-button')


class ProductsPageLocators:
    PRODUCT_HEADER = (By.CLASS_NAME, 'title')
    CART_BUTTON = (By.ID, 'shopping_cart_container')
    PRODUCT_1 = (By.ID, 'add-to-cart-sauce-labs-backpack')
    MENU = (By.ID, 'react-burger-menu-btn')
    ABOUT_LINK = (By.ID, 'about_sidebar_link')

class CartPageLocators:
    CHECKOUT_BUTTON = (By.ID, 'checkout')


class ClientInformationPageLocators:
    FIRST_NAME = (By.ID, 'first-name')
    LAST_NAME = (By.ID, 'last-name')
    POSTAL_CODE = (By.ID, 'postal-code')
    CONTINUE_BUTTON = (By.ID, 'continue')


class PaymentPageLocators:
    FINISH_BUTTON = (By.ID, 'finish')