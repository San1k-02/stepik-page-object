from pages.basket_page import BasketPage
from pages.product_page import ProductPage

def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link="http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page=ProductPage(browser,link)
    page.open()
    page.go_to_basket()
    basket_page=BasketPage(browser,browser.current_url)
    basket_page.basket_is_empty_message()
    basket_page.no_goods_in_basket()
    

# @pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
#                                   pytest.param(7, marks=pytest.mark.xfail),
#                                   8, 9])

# def test_guest_can_add_product_to_basket(browser,link):
#     link=f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
#     page=ProductPage(browser,link)
#     page.open()
#     page.add_to_cart()
#     page.solve_quiz_and_get_code()
#     page.should_be_message_book()
#     page.should_be_price()

# def test_guest_should_see_login_link_on_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.should_be_login_link()

# def test_guest_can_go_to_login_page_from_product_page(browser):
#     link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
#     page = ProductPage(browser, link)
#     page.open()
#     page.go_to_login_page()

# def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
#     link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/   "
#     page=ProductPage(browser,link)
#     page.open()
#     page.add_to_cart()
#     #page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()
#     #time.sleep(60)

# def test_guest_cant_see_success_message(browser):
#     link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page=ProductPage(browser,link)
#     page.open()
#     #page.solve_quiz_and_get_code()
#     page.should_not_be_success_message()

# def test_message_disappeared_after_adding_product_to_basket(browser):
#     link="http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
#     page=ProductPage(browser,link)
#     page.open()
#     page.add_to_cart()
#     #page.solve_quiz_and_get_code()
#     page.should_disappear()