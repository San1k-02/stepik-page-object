from pages.base_page import BasePage
from pages.locators import LoginPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        #self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Wrong url"
        #assert True

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "No login email entry field"
        assert self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "No login password entry field"
        #assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "No registration email entry field"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "No registration password1 entry field"
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD1), "No registration password2 entry field"
        #assert True