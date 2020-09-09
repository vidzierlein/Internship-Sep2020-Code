"""
Learn to click a button with Selenium

DISCLAIMER: This code is aimed at Selenium BEGINNERS
For more advanced tutorials and to learn how Qxf2 writes GUI automation, please visit our:
a) Our GUI automation guides: http://qxf2.com/gui-automation-diy
b) Other GitHub repos: https://github.com/qxf2

AUTHOR: Avinash Shetty
Contact: avinash@qxf2.com

SCOPE:
1) Launch Chrome driver
2) Navigate to Qxf2 Tutorial page
3) Find the Click me! button and click on it
4) Close the driver
"""
import time
from selenium import webdriver

driver = webdriver.Chrome()

driver.maximize_window()

driver.get("http://qxf2.com/selenium-tutorial-main")
name = driver.find_element_by_xpath("//input[@id='name']")
name.send_keys('vid')

button = driver.find_element_by_xpath("//button[@type='submit']")
button.click()

time.sleep(3)

driver.close()

