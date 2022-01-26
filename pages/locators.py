from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    INPUT_EMAIL = (By.CSS_SELECTOR, "[name = 'registration-email']")
    INPUT_PASSWORD1 = (By.CSS_SELECTOR, "[name = 'registration-password1']")
    INPUT_PASSWORD2 = (By.CSS_SELECTOR, "[name = 'registration-password2']")
    REGISTRATION_SUBMIT = (By.CSS_SELECTOR, "[name = 'registration_submit")


class ProductPageLocators():
    PRODUCT_NAME = (By.CSS_SELECTOR, ".col-sm-6.product_main h1")
    PRODUCT_PRICE = (By.CSS_SELECTOR, ".product_main .price_color")
    ADD_TO_BASKET_BUTTON = (By.CLASS_NAME, "btn.btn-lg.btn-primary.btn-add-to-basket")
    PRODUCT_ADDED_ALERT = (By.CSS_SELECTOR, ".alert-success .alertinner strong")
    PRODUCT_ADDED_PRICE = (By.CSS_SELECTOR, ".alert-info .alertinner strong")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    BASKET_LINK = (By.XPATH, '//*[@id="default"]/header/div[1]/div/div[2]/span/a')
    EMPTY_BASKET = (By.CSS_SELECTOR, '.basket-title.hidden-xs')
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, '#content_inner >p')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")
