import time
from itertools import count

from selenium import webdriver
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
driver.implicitly_wait(3)
driver.maximize_window()
print("Browser Launched")
name = "Rajesh"
expectedList = ['Cucumber - 1 Kg', 'Raspberry - 1/4 Kg', 'Strawberry - 1/4 Kg']
actualList = []
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys("ber")
time.sleep(3)

results = driver.find_elements(By.XPATH,"//div[@class='products']/div")#List[]
count = len(results)
assert count > 0
for result in results:
    #chaining of web elements
    actualList.append(result.find_element(By.XPATH,"h4").text)
    result.find_element(By.XPATH,"div/button").click()

assert  expectedList == actualList
driver.find_element(By.CSS_SELECTOR,"img[alt='Cart']").click()

driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()
#sum validation
prices = driver.find_elements(By.CSS_SELECTOR,"tr td:nth-child(5) p")
sum = 0
for price in prices:
    sum = sum + int(price.text)
print(sum)

totalamt = int(driver.find_element(By.CSS_SELECTOR,".totAmt").text)
assert  sum ==  totalamt

driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys("rahulshettyacademy")

driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"promoInfo")))
print(driver.find_element(By.CLASS_NAME,"promoInfo").text)
totalAfterDiscount = float(driver.find_element(By.CSS_SELECTOR,".discountAmt").text)
print(totalAfterDiscount)
assert totalAfterDiscount < totalamt

