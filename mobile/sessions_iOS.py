from appium import webdriver
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
driver.quit()