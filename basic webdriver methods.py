from selenium import webdriver
from selenium.webdriver.chrome.service import Service
driver = webdriver.Chrome(service=Service("/Library/Frameworks/Python.framework/Versions/3.10/chromedriver"))
driver.get('https://www.selenium.dev/')
driver.maximize_window()
print(driver.title)
print(driver.current_url)
driver.get("https://www.selenium.dev/about/")
driver.minimize_window()
driver.back()
driver.refresh()
driver.close()
