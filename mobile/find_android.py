from appium import webdriver

#need to improt this to get the locator strategies to use
from appium.webdriver.common.appiumby import AppiumBy

#need to improt this to get the webdriver wait function
from selenium.webdriver.support.wait import WebDriverWait

#need to import this to set the expected conditions for the webdriver
from selenium.webdriver.support import expected_conditions

#import this to set expected conditions for the appium XCUItest options
from appium.options.ios import XCUITestOptions

from appium.options.android import UiAutomator2Options

#need to teach our script where the app is located
from os import path

#absolute path to directory where app is, variable, __file__ is a magic variable where the file is 
#encountered
CUR_DIR = path.dirname(path.abspath(__file__))
#print(CUR_DIR)

#get the actual path to application file (joins the different path segments, 
#then we get the full path dir and file)
APP = path.join(CUR_DIR, 'TheApp.apk')

#print(APP)
#location of appium server, where is it listening for requests (we need to start Appium server from terminal)
# run appium command in Terminal
APPIUM = "http://localhost:4723"

#define capabilities dictonary
appium_server_url = 'http://localhost:4723'
options = UiAutomator2Options()
options.platformName = "Android"
#options.platformVersion = "13"
#options.deviceName = "Appium Test"
options.automationName = "UiAutomator2"
options.app = APP

driver = webdriver.Remote(APPIUM, options=options)


try: 
    #we need to wait some time for all elements to load
    wait = WebDriverWait(driver, 10)

    #wait until the "Login Screen" accessibility ID element is loaded
    wait.until(expected_conditions.presence_of_all_elements_located((AppiumBy.ACCESSIBILITY_ID,'Login Screen')))
    
    #try to find element by it's class name (type) : UI class name for anything that is a static type element (simple text label)
    driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.TextView')
    
    driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Webview Demo']")

finally:
    driver.quit()