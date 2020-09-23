import pytest
from pages.base_page import BasePage
from pages.main_page import MainPage

main_link = "https://itsecurity.ru/"


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    def test_guest_can_see_main_page(self, browser):
        page = MainPage(browser, main_link)
        page.open()

