from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), "BASKET IS NOT EMPTY"

    def should_be_text_basket_empty(self):
        assert self.is_element_present(*BasketPageLocators.TEXT_BASKET_EMPTY), "BASKET IS NOT EMPTY"
