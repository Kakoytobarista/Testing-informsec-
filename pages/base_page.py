from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators
from pages.locators import LoginPageLocators
from pages.private_value import password
from pages.private_value import email


class BasePage(object):
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False, "element is not present"
        return True

    def go_to_feedback_page(self):
        link = self.browser.find_element(*MainPageLocators.ASK_MANAGER)
        link.click()

    def go_to_login_page(self):
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def register_on_login_page(self):
        input1 = self.browser.find_element(*LoginPageLocators.LOGIN_USER_SELECTOR)
        input1.send_keys(email)
        input2 = self.browser.find_element(*LoginPageLocators.PASSWORD_USER_SELECTOR)
        input2.send_keys(password)
        self.browser.find_element(*LoginPageLocators.BUTTON_LOGIN_SELECTOR).click()

    def go_to_course_catalog_page(self):
        link = self.browser.find_element(*MainPageLocators.CATALOG_COURSE)
        link.click()

