from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
driver = webdriver.Chrome(service=Service("/Library/Frameworks/Python.framework/Versions/3.10/chromedriver"))
driver.get('https://the-internet.herokuapp.com/windows')
driver.find_element(By.LINK_TEXT,"Click Here").click()
childwindow = driver.window_handles[1]
driver.switch_to.window(childwindow)
print(driver.find_element(By.TAG_NAME,"H3").text)
driver.close()
driver.switch_to.window(driver.window_handles[0])
print(driver.find_element(By.TAG_NAME,"H3").text)
assert "Opening a new window" in driver.find_element(By.TAG_NAME,"H3").text