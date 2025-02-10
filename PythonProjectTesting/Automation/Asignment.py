import time
from itertools import count

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.ie.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait

#Chrome driver service Selenium 160 -> `60 chrome driver
#if chrome driver is not update and need to connect with VPN then in this case we need to download
#the chrome from google then pass driver path in
"""service_obj = Service("")
driver=webdriver.Chrome(services=service_obj)"""

driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.LINK_TEXT,"Free Access to InterviewQues/ResumeAssistance/Material").click()
windowOpened=driver.window_handles
driver.switch_to.window(windowOpened[1])
email = driver.find_element(By.XPATH,"//a[text()='mentor@rahulshettyacademy.com']").text
print(email)
driver.close()
driver.switch_to.window(windowOpened[0])
driver.find_element(By.ID,"username").send_keys(email)
driver.find_element(By.ID,"password").send_keys("Test123")
driver.find_element(By.ID,"signInBtn").click()
alertmessage = driver.find_element(By.CSS_SELECTOR,"alert alert-danger col-md-12").text
print(alertmessage)