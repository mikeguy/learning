import time
from appium import webdriver

#need to improt this to get the locator strategies to use
from appium.webdriver.common.appiumby import AppiumBy

#need to improt this to get the webdriver wait function
from selenium.webdriver.support.wait import WebDriverWait

#need to import this to set the expected conditions for the webdriver
from selenium.webdriver.support import expected_conditions

#import this to set expected conditions for the appium XCUItest options
from appium.options.ios import XCUITestOptions

#need to teach our script where the app is located
from os import path

#absolute path to directory where app is, variable, __file__ is a magic variable where the file is 
#encountered
CUR_DIR = path.dirname(path.abspath(__file__))
#print(CUR_DIR)

#get the actual path to application file (joins the different path segments, 
#then we get the full path dir and file)
APP = path.join(CUR_DIR, 'TheApp.app.zip')

#print(APP)
#location of appium server, where is it listening for requests (we need to start Appium server from terminal)
# run appium command in Terminal
APPIUM = "http://localhost:4723"

#define capabilities dictonary
appium_server_url = 'http://localhost:4723'
options = XCUITestOptions()
options.platformName = "iOS"
options.platformVersion = "16.4"
options.deviceName = "iPhone 14"
options.automationName = "XCUITest"
options.app = APP

driver = webdriver.Remote(APPIUM, options=options)


try:
     
    #not sure why static wait needs to be used here instead of  wait = WebDriverWait(driver, 10)? are we not waiting for 10 seconds here?
    time.sleep(4)
    #print the page source of the app
    print(driver.page_source)


finally:
    driver.quit()