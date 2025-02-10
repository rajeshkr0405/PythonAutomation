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
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
action = ActionChains(driver)
#action.double_click for double click on elements
#action.context_click() for right click
#action.drag_and_drop()
action.move_to_element(driver.find_element(By.ID,"mousehover")).perform()
#action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform()
