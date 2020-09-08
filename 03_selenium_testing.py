import time
from selenium import webdriver

driver = webdriver.Chrome()

#driver.maximize_window()

driver.get("http://qxf2.com/selenium-tutorial-main")
name = driver.find_element_by_xpath("//input[@id='name']")
name.send_keys('Avinash')




dropdown_element = driver.find_element_by_xpath("//button[@data-toggle='dropdown']")
dropdown_element.click()

driver.find_element_by_xpath("//a[text()='Male]").click()

time.sleep(1)
driver.close()