from appium.webdriver.common.appiumby import AppiumBy #need to improt this to get the locator strategies to use
from views.base_views import BaseView
from selenium.common.exceptions import TimeoutException

class EchoView(BaseView):
    # = (locator strategy, selector)
    MESSAGE_INPUT = (AppiumBy.ACCESSIBILITY_ID, "messageInput")
    SAVE_BUTTON = (AppiumBy.ACCESSIBILITY_ID, "messageSaveBtn")
    

    
    
    def save_message (self, message):
        self.wait_for(self.MESSAGE_INPUT).send_keys(message)
        #click the save button
        self.find(self.SAVE_BUTTON).click()

    def read_message(self):
        #assert that the "hello" text is displayed
        try:
            return self.wait_for(self.MESSAGE_LABEL).text 
        except TimeoutException:
            return None
        
    def nav_back(self):
        from views.home_view import HomeView
        self.driver.back()
        return HomeView.instance(self.driver)
    
class EchoViewIOS(EchoView):
    MESSAGE_LABEL = (AppiumBy.ACCESSIBILITY_ID, "savedMessage")

class EchoViewAndroid(EchoView):
    MESSAGE_LABEL = (AppiumBy.XPATH, "//android.widget.TextView[@content-desc != '']")


EchoView._IOS = EchoViewIOS
EchoView._ANDROID = EchoViewAndroid
