#need to improt this to get the locator strategies to use
from appium.webdriver.common.appiumby import AppiumBy

#need to improt this to get the webdriver wait function
from selenium.webdriver.support.wait import WebDriverWait

#need to import this to set the expected conditions for the webdriver
from selenium.webdriver.support import expected_conditions

class HomeView(object):
    ECHO_ITEM = (AppiumBy.ACCESSIBILITY_ID,'Echo Box')

    def __init__(self,driver):
        self.driver = driver
    
    def nav_to_echo_box(self): 

        #wait for the "echo box element" and click to go to the next field
        wait.until(expected_conditions.presence_of_element_located((self.ECHO_ITEM))).click()
