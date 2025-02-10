import time

from selenium import webdriver
from selenium.webdriver.ie.service import Service

#Chrome driver service Selenium 160 -> `60 chrome driver
#if chrome driver is not update and need to connect with VPN then in this case we need to download
#the chrome from google then pass driver path in
"""service_obj = Service("")
driver=webdriver.Chrome(services=service_obj)"""
driver = webdriver.Chrome()
time.sleep(2)
driver.maximize_window()
print("Browser Launched")
driver.get("https://rahulshettyacademy.com")
print(driver.title)
print(driver.current_url)
