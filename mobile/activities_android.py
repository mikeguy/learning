from appium import webdriver
from appium.options.android import UiAutomator2Options
import time

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

app = path.join(CUR_DIR, "ApiDemos.apk")
app_id = "io.appium.android.apis"
app_act1 = ".graphics.TOuchPaint"
app_act2 = ".text.Marquee"

try: 
    driver.install_app(app)
    
    #very fast way to accelerate the testing because you do not need to navigate to the location where you want to test
    #if you add . appium knows to add pakage loaded
    #driver.start_activity(app_id, app_act1)
    driver.startActivity(app_id, app_act1)
    time.sleep(1)
    driver.start_session(app_id, app_act2)
    time.sleep(1)

finally:
    driver.quit()