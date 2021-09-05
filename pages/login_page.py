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
        assert self.is_element_present(*LoginPageLocators.Login_email), "No login email entry field"
        assert self.is_element_present(*LoginPageLocators.Login_password), "No login password entry field"
        #assert True

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.Registration_email), "No registration email entry field"
        assert self.is_element_present(*LoginPageLocators.Registration_password1), "No registration password1 entry field"
        assert self.is_element_present(*LoginPageLocators.Registration_password2), "No registration password2 entry field"
        #assert True