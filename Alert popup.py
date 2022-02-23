import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
validation_text ="Man"

driver = webdriver.Chrome(service=Service("/Library/Frameworks/Python.framework/Versions/3.10/chromedriver"))
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_element(By.CSS_SELECTOR,"#name").send_keys("Man")
driver.find_element(By.ID,"alertbtn").click()
alert = driver.switch_to.alert
alert_Text = (alert.text)
assert validation_text in alert_Text
time.sleep(2)
alert.accept()