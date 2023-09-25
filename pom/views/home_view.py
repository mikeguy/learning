#need to improt this to get the locator strategies to use
from appium.webdriver.common.appiumby import AppiumBy

#need to improt this to get the webdriver wait function
from selenium.webdriver.support.wait import WebDriverWait

#need to import this to set the expected conditions for the webdriver
from selenium.webdriver.support import expected_conditions

class HomeView(object):
    
    def nav_to_echo_box(self): 
        #we need to wait some time for all elements to load
        wait = WebDriverWait(driver, 10)
        
        #wait for the "echo box element" and click to go to the next field
        wait.until(expected_conditions.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,'Echo Box'))).click()
