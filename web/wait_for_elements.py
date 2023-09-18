from selenium import webdriver
from selenium.webdriver.common.by import By

from selenium.webdriver.support.wait import WebDriverWait

#the as EC lets us import a condition and use it as the name EC!!! you can do expected_conditions as EC
from selenium.webdriver.support import expected_conditions


driver = webdriver.Firefox()

try:
    wait = WebDriverWait(driver, 10)

    driver.get("https://the-internet.herokuapp.com/")
    wait.until(expected_conditions.presence_of_all_elements_located((By.LINK_TEXT, "Form Authentication")))
    print(driver.current_url)
    wait.until(expected_conditions.url_to_be("https://the-internet.herokuapp.com/"))    
finally:
    driver.quit()