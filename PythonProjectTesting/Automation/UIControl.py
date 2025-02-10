import time

from selenium import webdriver
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select


#Chrome driver service Selenium 160 -> `60 chrome driver
#if chrome driver is not update and need to connect with VPN then in this case we need to download
#the chrome from google then pass driver path in
"""service_obj = Service("")
driver=webdriver.Chrome(services=service_obj)"""

driver = webdriver.Chrome()
driver.implicitly_wait(3)
driver.maximize_window()
print("Browser Launched")
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
checkBoxes= driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkBoxes))
for checkbox in checkBoxes:
    if checkbox.get_attribute("value") == "option2":
        checkbox.click()
        assert checkbox.is_selected()
        break