from selenium.webdriver.support.wait import WebDriverWait #need to improt this to get the webdriver wait function
from selenium.webdriver.support import expected_conditions #need to import this to set the expected conditions for the webdriver

#this will be the base class for all other view classes
class BaseView(object):

    def __init__(self,driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def wait_for(self, locator):
        return self.wait.until(expected_conditions.presence_of_element_located((locator)))
    
    def find(self, locator):
        return self.driver.find_element(*locator)