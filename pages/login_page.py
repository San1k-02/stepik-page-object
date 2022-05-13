from .base_page import BasePage
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def register_new_user(self, email, password):
        self.email = email
        self.password = password
        email = str(int(time.time())) + "@fakemail.org"
        password = str(int(time.time()))
        btn = self.browser.find_element(*LoginPageLocators.INPUT_ID_REGISTRATION_EMAIL)
        btn.send_keys(email)
        btn = self.browser.find_element(*LoginPageLocators.INPUT_ID_REGISTRATION_PASSWORD1)
        btn.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.INPUT_ID_REGISTRATION_PASSWORD2)
        btn.send_keys(password)
        btn = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTRATION_SUBMIT)
        btn.click()
        time.sleep(2)

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert '/login' in self.browser.current_url, "LOGIN_LINK IS FALSE"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "LOGIN_FORM IS NOT PRESENTED"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "REGISTER_FORM IS NOT PRESENTED"
