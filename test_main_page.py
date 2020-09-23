import pytest
from pages.base_page import BasePage
from pages.other_page import MainPageAsserts
from pages.main_page import MainPage

main_link = "https://itsecurity.ru/"


@pytest.mark.login_guest
class TestLoginFromMainPage():
    def test_guest_can_go_to_main_page(self, browser):
        page = MainPage(browser, main_link)
        page.open()

    def test_guest_can_ask_the_manager_a_question(self, browser):
        page = MainPageAsserts(browser, main_link)
        page.open()
        page.go_to_feedback_page()
        page.should_see_ask_questions_manager()
