from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(service=Service("/Library/Frameworks/Python.framework/Versions/3.10/chromedriver"))
driver.get('https://rahulshettyacademy.com/angularpractice/')
#driver.find_element(By. NAME,"name").send_keys("Gopika")
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Gopika")
driver.find_element(By.NAME,"email").send_keys("gopika.k.1993@gmail.com")
driver.find_element(By.CLASS_NAME,"form-check-label").click()
driver.find_element(By.ID,"exampleInputPassword1").send_keys("Password")
driver.find_element(By.XPATH,"//input[@type='submit']").click()