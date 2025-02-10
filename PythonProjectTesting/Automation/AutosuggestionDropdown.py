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
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("Ind")
time.sleep(2)
Countries= driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(Countries))
for Country in Countries :
    if Country.text == "India":
        Country.click()
        break
#print(driver.find_element(By.ID,"autosuggest").text)
assert driver.find_element(By.ID,"autosuggest").get_attribute("value") == "India"
driver.find
origin = driver.find_elements(By.CSS_SELECTOR,"div[class='dropdownDiv'] ul li a")
print(len(origin))
