
import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
# Navigate to Qxf2 Tutorial page
driver.get("http://qxf2.com/selenium-tutorial-main")

# Find the click me! button and click it
button  = driver.find_element_by_xpath("//button[text()='Click me!']")  
button.click()
# Pause the script to wait for validation messages to load
time.sleep(3)

try:
    driver.find_element_by_xpath("//input[@type='mail']")
except Exception:
    result_flag = False
else:
    result_flag = True
if result_flag is True:
    print("Validation message for email present")
else:
    print("Validation message for email NOT present")

driver.close()
    
