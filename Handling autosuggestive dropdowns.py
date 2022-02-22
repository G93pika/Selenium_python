import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(service=Service("/Library/Frameworks/Python.framework/Versions/3.10/chromedriver"))
driver.get('https://rahulshettyacademy.com/dropdownsPractise/')
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)
countries = driver.find_elements( By.CSS_SELECTOR,("li[class='ui-menu-item'] a" ))
print(len(countries))
for country in countries:
    if country.text == "India":
        country.click()
        break
time.sleep(2)
assert driver.find_element(By.ID,"autosuggest").get_attribute('value')=="India"
#driver.quit()