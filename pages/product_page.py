from pages.base_page import BasePage
from pages.locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_cart(self):
        add_to_cart_button = self.browser.find_element(*ProductPageLocators.ADD_TO_CART_BUTTON)
        add_to_cart_button.click()
    
    def should_be_message_book(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_MESSAGE).text == \
               self.browser.find_element(*ProductPageLocators.NAME_BOOK).text, "Wrong product"

    def should_be_price(self):
        assert self.browser.find_element(*ProductPageLocators.PRICE_MESSAGE).text == \
               self.browser.find_element(*ProductPageLocators.PRICE).text, "Wrong price"
