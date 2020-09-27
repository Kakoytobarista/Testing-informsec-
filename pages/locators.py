from selenium.webdriver.common.by import By


class MainPageLocators(object):
    ASK_MANAGER = (By.CSS_SELECTOR, "body > div.but-user > ul")
    LOGIN_LINK = (By.CSS_SELECTOR, "body > div.main > div.header > div.b-input > ul > li.input > span > a")
    CATALOG_COURSE = (By.CSS_SELECTOR, "body > div.main > div.panel-top > div > \
    div.menu-top > ul > li:nth-child(1) > a")



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
