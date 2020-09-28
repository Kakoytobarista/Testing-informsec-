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
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver

email1 = "gurbanov@rambler.ru"


class BasePage(object):
    def __init__(self, browser, url, timeout=15):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        self.browser.get(self.url)
        print("\nopen page")

    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except NoSuchElementException:
            return False, "element is not present"
        return True

    def is_not_element_present(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

    def is_disappeared(self, how, what, timeout=4):
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True
        return False

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

    def click_to_edu(self, driver):
        element = driver.find_element_by_xpath("//*[@id='jvlabelWrap']/jdiv[2]/jdiv")
        driver.execute_script("arguments[0].click();", element)
        print("\nclick on tab")

    def fill_in_the_email(self, browser):
        input1 = self.browser.find_element(*MainPageLocators.FILL_THE_EMAIL)
        input1.send_keys(email)
        button = browser.find_element_by_class_name("sendButton_33e")
        button.click()
        print("\nclick and send message")
        input2 = self.browser.find_element(*MainPageLocators.FILL_FOR_EDU)
        input2.send_keys(email)
        print("\nsend email")
        input3 = self.browser.find_element(*MainPageLocators.FILL_FOR_EDU3)
        input3.click()
        print('\nclick at the button')
        assert self.is_not_element_present(*MainPageLocators.MESSAGE_AFTER_ALL_PROCEDURE), "should see nothing"

    def fill_the_email2(self):
        input4 = self.browser.find_element(*MainPageLocators.MESSAGE_AFTER_ALL_PROCEDURE).get_attribute('textContent')
        print(input4)
        assert input4 == "Спасибо!", "should be another words"
        time.sleep(5)
