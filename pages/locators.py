from selenium.webdriver.common.by import By
from selenium import webdriver


class MainPageLocators(object):
    ASK_MANAGER = (By.CSS_SELECTOR, "body > div.but-user > ul")
    LOGIN_LINK = (By.CSS_SELECTOR, "body > div.main > div.header > div.b-input > ul > li.input > span > a")
    CATALOG_COURSE = (By.CSS_SELECTOR, "body > div.main > div.panel-top > div > \
    div.menu-top > ul > li:nth-child(1) > a")
    BUTTON_AT_EDU = (By.CSS_SELECTOR, "#jvlabelWrap > jdiv.hoverl_e8c")
    FILL_THE_EMAIL = (By.CSS_SELECTOR, "#jcont > jdiv.contentWrapper_22c > jdiv > jdiv.input_878.show_fa0 > jdiv"
                                       " > jdiv.tdTextarea_bac > textarea")
    FEEDBACK_FROM_EDU = (By.XPATH, "//*[@id='scrollbar-container']/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/"
    "jdiv[3]/jdiv/text()")

    BUTTON_FOR_EDU = (By.CSS_SELECTOR, "#jcont > jdiv.contentWrapper_22c > jdiv > jdiv.input_878.show_fa0 > jdiv > "
                                       "jdiv:nth-child(2) > jdiv")

    FILL_FOR_EDU = (By.CSS_SELECTOR, "#scrollbar-container > jdiv:nth-child(1) > jdiv > jdiv.box_e16 \
                                     > jdiv > jdiv > jdiv.overlay_6f8")

    FIL_FOR_EDU2 = (By.XPATH, "//*[@id='scrollbar-container']/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input")
    FIL_FOR_EDU3 = (By.XPATH, "//*[@id='scrollbar-container']/jdiv[1]/jdiv/jdiv[4]/jdiv/jdiv/jdiv/jdiv/jdiv[1]/input")


class OtherPageLocators(object):
    PAGE_WITH_FEEDBACK_FROM_MANAGER = (By.CSS_SELECTOR, "body > div.main > div.content > h1")
    PAGE_WITH_CATALOG_COURSE = (By.CSS_SELECTOR, "body > div.main > div.content > h1")


class LoginPageLocators(object):
    LOGIN_FORM = (By.CSS_SELECTOR, "body > div.main > div.content > div.inner > div > div:nth-child(1) > div > form")
    LOGIN_USER_SELECTOR = (By.CSS_SELECTOR, "body > div.main > div.content > div.inner > div > div:nth-child(1) >"
                                            " div > form > div:nth-child(3) > input[type=text]")
    PASSWORD_USER_SELECTOR = (By.CSS_SELECTOR, "body > div.main > div.content > div.inner > div > div:nth-child(1) >"
                                               " div > form > div:nth-child(4) > input[type=password]")
    BUTTON_LOGIN_SELECTOR = (By.CSS_SELECTOR, "body > div.main > div.content > div.inner > div > div:nth-child(1) > "
                                              "div > form > div.button.auth-submit")
    SUCCESSFUL_LOGIN = (By.CSS_SELECTOR, "body > div.main > div.content > div.color > h2")
