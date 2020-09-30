from .base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators
from selenium import webdriver


# class MainPageInit(BasePage):
#     def __init__(self, *args, **kwargs):
#         super(MainPageInit, self).__init__(*args, **kwargs)


class MainPage(BasePage):
    def should_be_main_url(self):
        str_url = self.url
        print(str_url)
        assert "https://itsecurity.ru/" in str_url, "main page do not find in URL"

    def should_see_thx(self):
        assert self.is_element_present(*MainPageLocators.FEEDBACK_FROM_EDU), \
            "should be thanks"

    def should_element_is_disappear(self):
        assert self.is_disappeared(*MainPageLocators.FILL_FOR_EDU), \
            "element not found"

    def should_element_is_not_present(self):
        assert self.is_not_element_present(*MainPageLocators.FILL_FOR_EDU), \
            "element is not present"
        print("\ncheck element is not present")

    def should_see_correct_information_on_main_page(self):
        inform = self.browser.find_element(*MainPageLocators.INFORMATION_AT_TOP).get_attribute('textContent')
        print('\nnumber', inform)
        assert inform == "+7 (495) 980-23-45 (*04)  edu@itsecurity.ru", 'should be another number'

    def should_see_correct_information_at_bottom_on_main_page(self, driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        inform1 = self.browser.find_element(*MainPageLocators.INFORMATION_AT_BOTTOM1).get_attribute('textContent')
        print(inform1)
        assert inform1 == "127018, Москва, Образцова, д.38, стр.1  Схема проезда", 'should be another'
        inform2 = self.browser.find_element(*MainPageLocators.INFORMATION_AT_BOTTOM2).get_attribute('textContent')
        print(inform2)
        assert inform2 == "(495) 980-2345 доб. 04", 'should be another'
        inform3 = self.browser.find_element(*MainPageLocators.INFORMATION_AT_BOTTOM3).get_attribute('textContent')
        print(inform3)
        assert inform3 == "edu@itsecurity.ru", 'should be another'

    def test_guest_should_see_news(self, driver):
        assert self.is_element_present(*MainPageLocators.TABLE_OF_NEWS), "table with news not found"
        # driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        driver.execute_script("window.scrollTo(0, 400)")
        assert self.is_element_present(*MainPageLocators.TABLE_WITH_SCHEDULE_COURSES), \
            "should be schedule courses"
