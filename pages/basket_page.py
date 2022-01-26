from .base_page import BasePage
from .locators import BasePageLocators

class BasketPage(BasePage):
    def should_be_empty_basket(self):
        assert self.is_not_element_present(*BasePageLocators.EMPTY_BASKET), 'Basket is not empty'

    def should_be_empty_basket_message(self):
        assert self.is_element_present(*BasePageLocators.EMPTY_BASKET_MESSAGE), 'There is no message about empty basket'
