#pytest convention starts with test_xxx
#we are going to test the echobox of the app with pytest framework




#need to improt this to get the locator strategies to use
from appium.webdriver.common.appiumby import AppiumBy

#need to improt this to get the webdriver wait function
from selenium.webdriver.support.wait import WebDriverWait

#need to import this to set the expected conditions for the webdriver
from selenium.webdriver.support import expected_conditions

#PyTest looks for functions that becing with test_
def test_echo_box(driver):

    #we need to wait some time for all elements to load
    wait = WebDriverWait(driver, 10)

    #wait for the "echo box element" and click to go to the next field
    wait.until(expected_conditions.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,'Echo Box'))).click()

    #wait for the input field and type "Hello" in it
    wait.until(expected_conditions.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "messageInput"))).send_keys("Hello")

    #click the save button
    driver.find_element(AppiumBy.ACCESSIBILITY_ID, "messageSaveBtn").click()

    #assert that the "hello" text is displayed
    saved_text= driver.find_element(AppiumBy.ACCESSIBILITY_ID, "savedMessage").text
    assert saved_text == "Hello"

    #go back to the main screen
    driver.back()

    #go back to the eco box view (good idea to wait again because of transition views)
    wait.until(expected_conditions.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID,'Echo Box'))).click()

    #assert that the "hello" text is still displayed
    saved_text= wait.until(expected_conditions.presence_of_element_located((AppiumBy.ACCESSIBILITY_ID, "savedMessage"))).text
    assert saved_text == "Hello"