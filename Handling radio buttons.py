import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("/Library/Frameworks/Python.framework/Versions/3.10/chromedriver"))
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
driver.find_elements(By.XPATH, "//input[@type ='radio']")[1].click()
assert driver.find_elements(By.XPATH, "//input[@type ='radio']")[1].is_selected()

