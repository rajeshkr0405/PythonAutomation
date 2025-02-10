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
driver.get("https://rahulshettyacademy.com/angularpractice/")
driver.find_element(By.NAME,"name").send_keys("Rajesh")
email = driver.find_element(By.NAME,"email")
email.send_keys("TestCargo@gmail.com")
pwd = driver.find_element(By.XPATH,"//input[@type='password']")
pwd.send_keys("Test@123")
checkBox = driver.find_element(By.ID,"exampleCheck1")
checkBox.click()

genders = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
genders.select_by_visible_text("Male")

#genders.select_by_visible_text("Male")
"""for geneder in genders:
    if geneder.get_attribute("option") == "Male":
        geneder.click()
        break"""