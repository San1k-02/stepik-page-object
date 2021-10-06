from pages.base_page import BasePage
from pages.locators import BasketPageLocators

class BasketPage(BasePage):
    def basket_is_empty_message(self):
        assert self.is_not_element_present(*BasketPageLocators.REMOVE_FROM_BASKET_BUTTON), \
            "Remove button is presented, but should not be"

    def no_goods_in_basket(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_IS_EMPTY_MESSAGE),\
            "No message 'Your basket is empty'"