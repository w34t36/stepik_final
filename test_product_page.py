from .pages.main_page import MainPage
from .pages.login_page import LoginPage
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
import time
import pytest


@pytest.mark.parametrize('link', ['?promo=offer0', '?promo=offer1', '?promo=offer2', '?promo=offer3',
                                  '?promo=offer4', '?promo=offer5', '?promo=offer6',
                                  pytest.param('?promo=offer7', marks=pytest.mark.xfail), '?promo=offer8',
                                  '?promo=offer9'])
def test_guest_can_add_product_to_basket_promo(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/{link}"
    page = ProductPage(browser, link)
    page.open()
    product_name_before_adding, product_price_before_adding = page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_added_procuct_page(product_name_before_adding, product_price_before_adding)


@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0"
    page = ProductPage(browser, link)
    page.open()
    product_name_before_adding, product_price_before_adding = page.add_to_basket()
    page.solve_quiz_and_get_code()
    page.should_be_success_message()
    page.should_be_added_procuct_page(product_name_before_adding, product_price_before_adding)

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
@pytest.mark.xfail(reason="Negative case")
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()

@pytest.mark.xfail(reason="Negative case")
def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, link)
    page.open()
    page.add_to_basket()
    page.should_be_message_disappeared()

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    product_page = BasketPage(browser, browser.current_url)
    product_page.should_be_empty_basket()
    product_page.should_be_empty_basket_message()

link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        page = LoginPage(browser, link)
        page.open()
        page.go_to_login_page()
        page.register_new_user(str(time.time()) + "@fakemail.org", str(time.time()))
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, link)
        page.open()
        product_name_before_adding, product_price_before_adding = page.add_to_basket()
        page.should_be_success_message()
        page.should_be_added_procuct_page(product_name_before_adding, product_price_before_adding)
