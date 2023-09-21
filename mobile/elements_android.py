#finding and interacting with elements

from appium import webdriver

#need to improt this to get the locator strategies to use
from appium.webdriver.common.appiumby import AppiumBy

#need to improt this to get the webdriver wait function
from selenium.webdriver.support.wait import WebDriverWait

#need to import this to set the expected conditions for the webdriver
from selenium.webdriver.support import expected_conditions

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
    
    #wait for the "echo box element" and click to go to the next field
    wait.until(expected_conditions.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,'Echo Box'))).click()
    
    #wait for the input field and type "Hello" in it
    wait.until(expected_conditions.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "messageInput"))).send_keys("Hello")

    #click the save button
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "messageSaveBtn").click()

    #assert that the "hello" text is displayed
    saved_text= driver.find_element(AppiumBy.XPATH, "//android.widget.TextView[@text='Hello']").text
    assert saved_text == "Hello"

    #go back to the main screen
    driver.back()

    #go back to the eco box view (good idea to wait again because of transition views)
    wait.until(expected_conditions.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,'Echo Box'))).click()

    #assert that the "hello" text is still displayed
    saved_text= wait.until(expected_conditions.presence_of_element_located((AppiumBy.XPATH, "//android.widget.TextView[@text='Hello']"))).text
    assert saved_text == "Hello"

finally:
    driver.quit()