from appium.webdriver.common.appiumby import AppiumBy #need to improt this to get the locator strategies to use
from selenium.webdriver.support.wait import WebDriverWait #need to improt this to get the webdriver wait function
from selenium.webdriver.support import expected_conditions #need to import this to set the expected conditions for the webdriver

class EchoView(object):
    # = (locator strategy, selector)
    MESSAGE_INPUT = (AppiumBy.ACCESSIBILITY_ID, "messageInput")
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "messageSaveBtn")
    MESSAGE_LABEL = (AppiumBy.ACCESSIBILITY_ID, "savedMessage")

    def __init__(self,driver):
        self.driver = driver
    
    def save_message (self, message):
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located((self.MESSAGE_INPUT))).send_keys(message)
        #click the save button
        self.driver.find_element(self.SAVE_BUTTON).click()

    def read_message(self):
        #assert that the "hello" text is displayed
        return self.driver.find_element(self.MESSAGE_LABEL).text    
        
    def nav_back(self):
        self.driver.back()