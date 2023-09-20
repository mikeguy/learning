from appium import webdriver

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


CAPS = {
    "platformName": "iOS",
    "appium:automationName": "XCUITest",
    "appium:platformVersion": "16.4",
    "appium:app": APP,
    "deviceName": "iPhone 8"
        # not sure what this does "noReset": True
}

 # "$cloud:AppiumOptions": {
  #  "version": "2.0.0",
   # "automationVersion": "3.52.0",
    #"plugins": ["images"]
  #}

driver = webdriver.Remote(command_executor=APPIUM, options=CAPS)
driver.quit()