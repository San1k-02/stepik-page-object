from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_EMAIL=(By.CSS_SELECTOR,"#id_login-username")
    LOGIN_PASSWORD=(By.CSS_SELECTOR,"#id_login-password")

    REGISTRATION_EMAIL=(By.CSS_SELECTOR,"#id_registration-email")
    REGISTRATION_PASSWORD1=(By.CSS_SELECTOR,"#id_registration-password1")
    REGISTRATION_PASSWORD2=(By.CSS_SELECTOR,"#id_registration-password2")

class ProductPageLocators():
    ADD_TO_CART_BUTTON=(By.CSS_SELECTOR,".btn-add-to-basket")
    BASKET_MESSAGE = By.CSS_SELECTOR, "#messages>:nth-child(1) strong"
    NAME_BOOK = By.CSS_SELECTOR, ".product_main h1"
    PRICE_MESSAGE = By.CSS_SELECTOR, "#messages>:nth-child(3) strong"
    PRICE = By.CSS_SELECTOR, ".product_main .price_color"
    SUCCESS_MESSAGE=By.CSS_SELECTOR,".alertinner"