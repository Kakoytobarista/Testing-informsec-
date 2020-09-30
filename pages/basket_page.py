from .base_page import BasePage
from .locators import ProductPageLocators
from pages.base_page import BasePage
import time
from selenium import webdriver


class BasketPage(BasePage):
    def should_see_success_go_to_basket_page(self):
        print('\nchecking basket link')
        assert self.is_element_present(*ProductPageLocators.BASKET_STATUS), "should be 'Ваша корзина пуста'"

    def should_see_catalog_of_course(self):
        assert self.is_element_present(*ProductPageLocators.CATALOG_COURSES_STUFF), \
            "should be catalog of courses"

    def should_see_product_in_basket(self):
        check = self.browser.find_element(*ProductPageLocators.PRODUCT_IN_BASKET).get_attribute('textContent')
        print(check)
        assert check == "Профессиональная переподготовка по направлению «Информационная безопасность»"

    def should_see_information_after_add_to_basket_at_top_side(self):
        check = self.browser.find_element(*ProductPageLocators.BASKET_INFORMATION_AT_TOP_SIDE).get_attribute('textContent')
        print(check)
        assert "Пожалуйста, обратите внимание! Если вы указали для какого-то курса" in check, "should see another stuff"
