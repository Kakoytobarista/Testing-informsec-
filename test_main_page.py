import pytest
import allure
from allure_commons.types import AttachmentType
from pages.base_page import BasePage
from pages.other_page import MainPageAsserts
from pages.main_page import MainPage

main_link = "https://itsecurity.ru/"


@pytest.mark.login_guest
class TestLoginFromMainPage(object):
    @allure.feature('Open pages')
    @allure.story('Тестируем вход на страницу сайтй')
    @allure.severity('critical')
    def test_guest_can_go_to_main_page(self, browser):
        page = MainPage(browser, main_link)
        page.open()
        with allure.step('Делаем скриншот'):
            allure.attach(browser.get_screenshot_as_png(),
                          name="Screenshot", attachment_type=AttachmentType.PNG)

    @allure.feature('Open pages')
    @allure.story("Тестируем открытие окна диалога с менеджером")
    @allure.severity('blocker')
    def test_guest_can_ask_the_manager_a_question(self, browser):
        page = MainPageAsserts(browser, main_link)
        page.open()
        page.go_to_feedback_page()
        with allure.step('Делаем скриншот'):
            allure.attach(browser.get_screenshot_as_png(),
                          name="Screenshot", attachment_type=AttachmentType.PNG)
        page.should_see_ask_questions_manager()
