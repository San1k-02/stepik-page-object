from pages.locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class MainPage(BasePage): 
    def go_to_login_page(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Can't go to login page"

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "No login link"