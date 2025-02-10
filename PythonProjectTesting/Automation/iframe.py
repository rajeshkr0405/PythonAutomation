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
driver.get("http://the-internet.herokuapp.com/iframe")
driver.switch_to.frame("mce_0_ifr")
driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("This is a test")
driver.switch_to.default_content()
print(driver.find_element(By.CSS_SELECTOR,"h3").text)
