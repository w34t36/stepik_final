from .base_page import BasePage
from .locators import LoginPageLocators
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def add_to_basket(self):
        product_name_before_adding, product_price_before_adding = self.should_be_product_present()
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        return product_name_before_adding, product_price_before_adding

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def should_be_product_present(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_NAME), 'Product is not present'
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text, \
               self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def should_be_added_procuct_page(self, product_name_before_adding, product_price_before_adding):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_ALERT).text == product_name_before_adding, \
            "Product name is incorrect "
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_ADDED_PRICE).text == product_price_before_adding, \
            "Product price is incorrect"

    def should_be_success_message(self):
        assert self.is_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not presented"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is presented, but should not be"

    def should_be_message_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.SUCCESS_MESSAGE), \
            "Success message is not disappeared, but should not be"