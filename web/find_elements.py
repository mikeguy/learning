#wrap your find ine exception handling .nosuchelement when searching for elements that might not be there

from selenium import webdriver
from selenium.webdriver.common.by import By


driver = webdriver.Firefox()

try:
    driver.get("https://the-internet.herokuapp.com/")
    el = driver.find_element(By.LINK_TEXT, "Form Authentication")
    print(f"There is {str(el)} form authenticator find" )

    els = driver.find_elements(By.TAG_NAME, "a")
    print (f"There were {len(els)} anchor elements")

    els = driver.find_elements(By.TAG_NAME, "foo")
    print (f"There were {len(els)} foo elements")
    

finally:
    driver.quit()