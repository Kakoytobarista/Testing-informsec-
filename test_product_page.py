import pytest
from pages.base_page import BasePage
from pages.other_page import MainPageAsserts
from pages.main_page import MainPage
from pages.login_page import LoginPage
import time
from selenium import webdriver
from pages.basket_page import BasketPage
from selenium.webdriver import ActionChains


login_link = "https://itsecurity.ru/personal/"
main_link = "https://itsecurity.ru/"


class TestLoginFromMainPage(object):
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        self.page = BasePage(browser, main_link)
        self.page.open()
        self.page.go_to_login_page()
        self.page.register_on_login_page()
    #
    # def test_user_can_see_success_register(self, browser):
    #     page = LoginPage(browser, login_link)
    #     page.should_be_login_page()
    #
    # def test_user_can_see_register_information(self, browser):
    #     page = LoginPage(browser, login_link)
    #     page.should_be_register_information(browser)
    #
    # def test_user_can_go_to_basket_page(self, browser):
    #     page = BasketPage(browser, main_link)
    #     page.go_to_basket_page()
    #     page.should_see_success_go_to_basket_page()

    def test_user_can_add_course_in_basket(self, browser):
        page = BasketPage(browser, main_link)
        page.open()
        page.go_to_course_link_and_take_of_course_in_basket(browser)
        page.should_see_catalog_of_course()
        page.should_see_product_in_basket()
        page.should_see_information_after_add_to_basket_at_top_side()
