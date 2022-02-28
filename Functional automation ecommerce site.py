from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome(service=Service("/Library/Frameworks/Python.framework/Versions/3.10/chromedriver"))
driver.get('https://rahulshettyacademy.com/seleniumPractise/')
driver.implicitly_wait(5)
driver.find_element(By.CSS_SELECTOR, "input[type='search']").send_keys("ber")
count = len(driver.find_elements(By.XPATH, "//div[@class='products']/div"))
print(count)
assert count == 3
buttons = driver.find_elements(By.XPATH, "//div[@class='product-action']/button")
list =[]
for button in buttons:
    list.append(button.find_element(By.XPATH,"parent::div/parent::div/h4").text)
    button.click()
print(list)
driver.find_element(By.CSS_SELECTOR, "img[alt='Cart']").click()
driver.find_element(By.XPATH, "//div[@class='action-block']/button").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promocode")))
veggies = driver.find_elements(By.CLASS_NAME,"product-name")
veg_list =[]
for veg in veggies:
    veg_list.append((veg).text)
print(veg_list)
assert list == veg_list
original_value = (driver.find_element(By.CLASS_NAME,"discountAmt").text)
driver.find_element(By.CLASS_NAME, "promocode").send_keys("rahulshettyacademy")
driver.find_element(By.CLASS_NAME, "promoBtn").click()
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "promoInfo")))
discount_value= (driver.find_element(By.CLASS_NAME,"discountAmt").text)
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
assert float(original_value)>float(discount_value)
print(original_value, " after discount is ", discount_value)
amts = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum = 0
for amt in amts:
    sum =sum + int(amt.text)
print(sum)
Total_amt = int(driver.find_element(By.CSS_SELECTOR,"span.totAMT").text)
assert sum == Total_amt