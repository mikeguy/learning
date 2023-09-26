from appium.webdriver.common.appiumby import AppiumBy #need to improt this to get the locator strategies to use
from views.base_views import BaseView
from views.echo_view import EchoView

class HomeView(BaseView):
    ECHO_ITEM = (AppiumBy.ACCESSIBILITY_ID,'Echo Box')
    
    def nav_to_echo_box(self): 
        self.wait_for(self.ECHO_ITEM).click()
        return EchoView(self.driver)