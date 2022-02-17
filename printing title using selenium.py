from selenium import webdriver

from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service= Service("/Library/Frameworks/Python.framework/Versions/3.10/chromedriver"))
driver.get( 'https://www.selenium.dev/' )
print(driver.title)
