from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

#the as EC lets us import a condition and use it as the name EC!!! you can do expected_conditions as EC (not using this here but just FYI)
from selenium.webdriver.support import expected_conditions


driver = webdriver.Firefox()

try:
    wait = WebDriverWait(driver, 10)

    #open website and click on the link with text "Form Authentication"
    driver.get("https://the-internet.herokuapp.com/")
    form_auth_link = wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Form Authentication")))
    print(driver.current_url)
    form_auth_link.click()

    #wait until the element #username is located (text field for username) and fill it with "tomsmith"
    username = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#username")))
    username.send_keys("tomsmith")

    # we do not need to use the wait.until here because this is already loaded guaranteed from the line above where we are waiting for the username, so the passoword field will load for sure
    password = driver.find_element(By.CSS_SELECTOR,"#password")
    password.send_keys("SuperSecretPassword!")

    #need to find sumbit button for form
    driver.find_element(By.CSS_SELECTOR,"button[type=submit]").click()

    #once the new page loads, search for the "Logout" link and click on it
    wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "Logout"))).click()

    #successifully logged out (FLASH message) check for the CSS selector named #flash and then check that "logged out" is in that text
    flash = wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, "#flash")))
    print (flash.text)
    assert "logged out" in flash.text
    
    #just making it fail on purpose
    assert "asdfg" in flash.text

finally:
    driver.quit()