from .base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators, OtherPageLocators


class MainPageAsserts(BasePage):
    def should_see_ask_questions_manager(self):
        assert self.is_element_present(*OtherPageLocators.PAGE_WITH_FEEDBACK_FROM_MANAGER), \
            "should see 'Задать вопрос менеджеру"

    def should_see_courses_page(self):
        self.should_be_course_page()
        self.should_be_catalog_course_url()

    def should_be_catalog_course_url(self):
        str.url = self.url
        print(str.url)
        assert 'catalog' in str.url, "should be catalog in url"

    def should_be_course_page(self):
        assert self.is_element_present(*OtherPageLocators.PAGE_WITH_CATALOG_COURSE), \
            "should be 'Курсы Учебного центра..'"

