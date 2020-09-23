from .base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators, OtherPageLocators


class MainPageAsserts(BasePage):
    def should_see_ask_questions_manager(self):
        assert self.is_element_present(*OtherPageLocators.PAGE_WITH_FEEDBACK_FROM_MANAGER), \
            "should see 'Задать вопрос менеджеру"
