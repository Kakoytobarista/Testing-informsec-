from selenium import webdriver
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators
from pages.locators import LoginPageLocators
from pages.locators import ProductPageLocators
from pages.private_value import password
from pages.private_value import email
from selenium.webdriver.common.keys import Keys
import time
from selenium import webdriver
import urllib.request
from selenium.webdriver import ActionChains
import pyautogui


email1 = "gurbanov@rambler.ru"
calendar1 = "30.09.2020"


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

    def go_to_basket_page(self):
        link = self.browser.find_element(*ProductPageLocators.BASKET_LINK)
        link.click()

    def go_to_course_link_and_take_of_course_in_basket(self, driver):
        link = self.browser.find_element(*ProductPageLocators.COURSE_PAGE)
        link.click()
        driver.execute_script("window.scrollTo(0, 250)")
        link1 = self.browser.find_element(*ProductPageLocators.COURSE_PRODUCT)
        link1.click()
        driver.execute_script("window.scrollTo(0, 1450)")
        print('\n to click')
        calendar = self.browser.find_element(*ProductPageLocators.CALENDAR_OF_COURSE)
        calendar.click()
        calendar.send_keys(calendar1)
        # print('\nclick to calendar')
        # time.sleep(3)
        # actions = ActionChains(driver)
        # actions.move_by_offset(220, 1920).click()
        # calendar.click()
        # time.sleep(3)
        button = self.browser.find_element(*ProductPageLocators.BUTTON_OF_CALENDAR)
        button.click()
        time.sleep(3)
        button2 = self.browser.find_element(*ProductPageLocators.BUTTON_TAKE_TO_BASKET)
        button2.click()
        time.sleep(3)

    def check_coordinate(self, driver):
        e = driver.find_element_by_xpath("//*[@id='table-wrap']/tbody/tr/td/div/div/div/div/div/a")
        location = e.location
        size = e.size
        print(location)
        print(size)
