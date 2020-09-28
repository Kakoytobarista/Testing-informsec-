import pytest
from pages.base_page import BasePage
from pages.other_page import MainPageAsserts
from pages.main_page import MainPage
from pages.login_page import LoginPage
import time


login_link = "https://itsecurity.ru/personal/"
main_link = "https://itsecurity.ru/"
from py.xml import html


@pytest.mark.login_guest
class TestFromMainPage(object):
    # def test_guest_can_go_to_main_page(self, browser):
    #     page = MainPage(browser, main_link)
    #     page.open()
    #     page.should_be_main_url()
    #
    # def test_guest_can_ask_the_manager_a_question(self, browser):
    #     page = MainPageAsserts(browser, main_link)
    #     page.open()
    #     page.go_to_feedback_page()
    #     page.should_see_ask_questions_manager()
    #
    # def test_guest_can_go_to_login_page(self, browser):
    #     page = MainPage(browser, main_link)
    #     page.open()
    #     login = LoginPage(browser, login_link)
    #     login.go_to_login_page()
    #     login.should_be_login_page()
    #
    # def test_guest_can_log_in(self, browser):
    #     page = LoginPage(browser, login_link)
    #     page.open()
    #     page.go_to_login_page()
    #     page.register_on_login_page()
    #     page.should_see_successful_login_in()
    #
    # @pytest.mark.parametrize('link', ["https://itsecurity.ru/",
    #                                   "https://itsecurity.ru/courses/",
    #                                   "https://itsecurity.ru/services/",
    #                                   "https://itsecurity.ru/informatsionnaya-bezopasnost-povyshenie-osvedomlennosti/",
    #                                   "https://itsecurity.ru/contacts/",
    #                                   "https://itsecurity.ru/study-center/"])
    # def test_guest_can_access_all_tabs(self, browser, link):
    #     page = BasePage(browser, link)
    #     page.open()
    def test_guest_can_write_to_edu(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        page.click_to_edu()
        page.fill_in_the_email(browser)
        page.should_element_is_not_present()

