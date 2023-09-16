from selenium import webdriver

#this is all we need to start a session, 
#selenium client library will start gecko, 
#construct set of capabilities
#send capabilites to appropriate route to server, 
#listen new session request resopnse and wrap session id properly
driver = webdriver.Firefox()


#this stops the session, runs a method on itself and closes the session ID
driver.quit()

