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
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.interaction import POINTER_TOUCH
from selenium.webdriver.common.actions.mouse_button import MouseButton
from selenium.webdriver.common.actions import interaction


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
    wait.until(expected_conditions.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,'List Demo'))).click()
    wait.until(expected_conditions.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, 'Altocumulus')))

   
    scroll = ActionBuilder(driver)
    finger = scroll.add_pointer_input("touch", "finger")
    finger.create_pointer_move(duration=0, x=100, y=500)
    finger.create_pointer_down(MouseButton.LEFT)
    finger.create_pointer_move(duration=250, x=10, y=-500, origin="pointer")
    finger.create_pointer_down(MouseButton.LEFT)
    #make all the actions happen at the same time
    scroll.perform()

    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "Stratocumulus")

finally:
    driver.quit()