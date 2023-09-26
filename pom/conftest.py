from appium import webdriver #need to teach our script where the app is located
from os import path
import pytest #import this to set expected conditions for the appium XCUItest options
from appium.options.ios import XCUITestOptions
from views.home_view import HomeView

#absolute path to directory where app is, variable, __file__ is a magic variable where the file is encountered
CUR_DIR = path.dirname(path.abspath(__file__))

#get the actual path to application file (joins the different path segments, then we get the full path dir and file)
APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.app.zip')

#location of appium server, where is it listening for requests (we need to start Appium server from terminal)
APPIUM = "http://localhost:4723"

#pytest fixture, turns a regular old python function into a pytest fixture
@pytest.fixture
def driver():
    options = XCUITestOptions()
    options.platformName = "iOS"
    options.platformVersion = "16.4"
    options.deviceName = "iPhone 14"
    options.automationName = "XCUITest"
    options.app = APP

    driver = webdriver.Remote(APPIUM, options=options)
    yield driver

    #exectue below code after test has completed
    driver.quit()
@pytest.fixture
def home(driver):
    return HomeView(driver)