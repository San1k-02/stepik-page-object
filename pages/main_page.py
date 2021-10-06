from pages.locators import BasePageLocators
from pages.base_page import BasePage
from pages.locators import BasePageLocators

class MainPage(BasePage):
#    def __init__(self, *args, **kwargs):
#         super(MainPage, self).__init__(*args, **kwargs)

    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        #self.browser.implicitly_wait(timeout)

    def go_to_basket_page(self):
        go_to_basket_button=self.browser.find_element(*BasePageLocators.GO_TO_BASKET_LINK)
        go_to_basket_button.click()
