from selenium.webdriver.common.by import By


class MainPageLocators(object):
    ASK_MANAGER = (By.CSS_SELECTOR, "body > div.but-user > ul")


class OtherPageLocators(object):
    PAGE_WITH_FEEDBACK_FROM_MANAGER = (By.CSS_SELECTOR, "body > div.main > div.content > h1")
