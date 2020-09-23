# import pytest
# from selenium import webdriver
# from selenium.webdriver.chrome.options import Options
#
#
# def pytest_adoption(parser):
#     parser.addoption('--browser_name', action='store', default="chrome",
#                      help="Choose browser: chrome or firefox")
#     parser.addoption('--language', action='store', default='en',
#                      help="Choose language: ru, en, ... (etc.)")
#
#
# @pytest.fixture(scope="function")
# def browser(request):
#     browser_name = request.config.getoption("browser_name")
#     user_language = request.config.getoption("language")
#     if browser_name == "chrome":
#         options = Options()
#         options.add_experimental_option('prefs',
#                                         {'intl.accept_languages': user_language})
#         print("\nstart chrome browser for test..")
#         browser = webdriver.Chrome(options=options)
#     elif browser_name == "firefox":
#         fp = webdriver.FirefoxProfile()
#         fp.set_preference("intl.accept_languages", user_language)
#         print("\nstart firefox browser for test..")
#         browser = webdriver.Firefox(fp)
#     else:
#         raise pytest.UsageError("--browser_name should be chrome or firefox")
#     browser.implicitly_wait(10)
#     yield browser
#     print("\nquit browser..")
#     browser.quit()

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                 help="Choose language")


@pytest.fixture(scope="function")
def browser(request):
    language = request.config.getoption("language")
    browser = webdriver.Chrome()
    options = Options()
    options.add_experimental_option('prefs', {'intl.accept_languages': language})
    yield browser
    browser = webdriver.Chrome(options=options)
    print("\nquit browser..")
    browser.quit()
