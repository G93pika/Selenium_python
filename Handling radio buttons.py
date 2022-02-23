from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=Service("/Library/Frameworks/Python.framework/Versions/3.10/chromedriver"))
driver.get('https://rahulshettyacademy.com/AutomationPractice/')
radio_buttons = driver.find_elements(By.XPATH, "//input[@type ='radio']")

for radio_button in radio_buttons:
     if radio_button.get_attribute("value") =="radio1":
        radio_button.click()
        assert radio_button.is_selected()