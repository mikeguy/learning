from appium import webdriver #need to teach our script where the app is located
from os import path
import pytest #import this to set expected conditions for the appium XCUItest options
from appium.options.ios import XCUITestOptions
from views.home_view import HomeView
from appium.options.android import UiAutomator2Options

#absolute path to directory where app is, variable, __file__ is a magic variable where the file is encountered
CUR_DIR = path.dirname(path.abspath(__file__))

#get the actual path to application file (joins the different path segments, then we get the full path dir and file)
IOS_APP = path.join(CUR_DIR, '..', 'mobile', 'TheApp.app.zip')

#get the actual path to android file
ANDROID_APP = path.join(CUR_DIR,  '..', 'mobile', 'TheApp.apk')

#location of appium server, where is it listening for requests (we need to start Appium server from terminal)
APPIUM = "http://localhost:4723"

IOS_CAPS = XCUITestOptions().load_capabilities({
    "platformName" : "iOS",
    "platformVersion" : "16.4",
    "deviceName" : "iPhone 14",
    "automationName" : "XCUITest",
    "app" : IOS_APP,
    })

ANDROID_CAPS = UiAutomator2Options().load_capabilities({
    "platformName" : "Android",
    "platformVersion" : "13",
    "automationName" : "UiAutomator2",
    "deviceName" : "Appium Test",
    "app" : ANDROID_APP,
    })

def pytest_addoption(parser):
    parser.addoption("--platform", action="store", default="ios")

@pytest.fixture
def platform(request):
    plat = request.config.getoption('platform').lower()
    if plat not in ["ios","android"]:
        raise ValueError("--platform value must be ios or android")
    return plat



#pytest fixture, turns a regular old python function into a pytest fixture
@pytest.fixture
def driver(platform):
    caps = IOS_CAPS if platform == "ios" else ANDROID_CAPS
    driver = webdriver.Remote(APPIUM, options=caps)
    
    driver._platform = platform
    yield driver

    #exectue below code after test has completed
    driver.quit()


@pytest.fixture
def home(driver):
    return HomeView(driver)