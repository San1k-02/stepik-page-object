from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    Login_email=(By.CSS_SELECTOR,"#id_login-username")
    Login_password=(By.CSS_SELECTOR,"#id_login-password")

    Registration_email=(By.CSS_SELECTOR,"#id_registration-email")
    Registration_password1=(By.CSS_SELECTOR,"#id_registration-password1")
    Registration_password2=(By.CSS_SELECTOR,"#id_registration-password2")