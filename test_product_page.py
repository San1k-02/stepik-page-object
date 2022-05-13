from pages.product_page import ProductPage
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
import pytest


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_msg_about_adding()
    page.should_be_add_to_basket_button()
    page.should_be_name_of_product()
    page.compare_basket_and_product_price()
    page.should_be_price_of_product()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.message_disappeared_after_adding_product_to_basket()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-city-and-the-stars_95/'
    page = BasketPage(browser, link)
    page.open()
    page.go_to_basket()
    page.should_be_basket_empty()
    page.should_be_text_basket_empty()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser, email=None, password=None):
        login_link = 'http://selenium1py.pythonanywhere.com/accounts/login/'
        page = LoginPage(browser, login_link)
        page.open()
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        product_link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207'
        page = ProductPage(browser, product_link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        product_link = 'http://selenium1py.pythonanywhere.com/en-gb/catalogue/coders-at-work_207'
        page = ProductPage(browser, product_link)
        page.open()
        page.add_product_to_basket()
        page.should_be_msg_about_adding()
        page.should_be_add_to_basket_button()
        page.should_be_name_of_product()
        page.compare_basket_and_product_price()
        page.should_be_price_of_product()
