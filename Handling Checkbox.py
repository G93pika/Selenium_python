import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import InvalidElementStateException

driver = webdriver.Chrome( service=Service( "/Library/Frameworks/Python.framework/Versions/3.10/chromedriver" ) )
driver.get( 'https://rahulshettyacademy.com/AutomationPractice/' )
checkboxes = driver.find_elements( By.XPATH, "//input[@type ='checkbox']" )
print( len( checkboxes ) )

#for checkbox in checkboxes:
   # checkbox.click()

for checkbox in checkboxes:
    if checkbox.get_attribute( "value" ) == "option2":
        checkbox.click()
