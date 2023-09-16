from selenium import webdriver

firefox_options = webdriver.FirefoxOptions()

try:
    driver = webdriver.Remote(
        command_executor='http://localhost:4444',
        options=firefox_options
    )
    driver.get("https://the-internet.herokuapp.com/")
finally:
    driver.quit() 

#try 
#finally