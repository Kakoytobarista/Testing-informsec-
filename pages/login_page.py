from.base_page import BasePage
from.locators import MainPageLocators
from.locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()

    def should_be_login_url(self):
        str_url = self.url
        print(str_url)
        assert 'personal' in str_url, "personal do not find in URL"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM)

    def should_see_successful_login_in(self):
        assert self.is_element_present(*LoginPageLocators.SUCCESSFUL_LOGIN), "should see 'Настройка личного кабинета'"

