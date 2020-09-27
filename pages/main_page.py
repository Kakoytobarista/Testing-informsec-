from .base_page import BasePage
from selenium.webdriver.common.by import By
from pages.locators import MainPageLocators


# class MainPage(BasePage):
#     def __init__(self, *args, **kwargs):
#         super(MainPage, self).__init__(*args, **kwargs)


class MainPage(BasePage):
    def should_be_main_url(self):
        str_url = self.url
        print(str_url)
        assert "https://itsecurity.ru/" in str_url, "main page do not find in URL"
