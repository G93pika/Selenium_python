from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome(service=Service("/Library/Frameworks/Python.framework/Versions/3.10/chromedriver"))
driver.get('https://rahulshettyacademy.com/seleniumPractise/')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR,"input[type='search']").send_keys("ber")
count=len(driver.find_elements(By.XPATH,"//div[@class='products']/div"))
print(count)
assert count == 3
buttons = driver.find_elements(By.XPATH,"//div[@class='product-action']/button")

for button in buttons:
    button.click()

driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()
driver.find_element(By.XPATH,"//div[@class='action-block']/button").click()
driver.find_element(By.CLASS_NAME,"promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME,"promoBtn").click()
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)