#Fill-Text-Fields

from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("https://www.google.com")

if(driver.title =="Google"):

    print("Success: Google search page launched successfully")
else:
    print("Failure: Google page Title is incorrect")

#xpath
search = driver.find_element_by_xpath("//input[@name='q']")
search.send_keys("qxf2 selenium")

submit = driver.find_element_by_xpath("//div[contains(@class,'FPdoLc')]/descendant::input[@aria-label='Google Search']")

print("Success")

time.sleep(3)


driver.close()

#//div[contains(@class,"FPdoLc")]/descendant::input[@aria-label="Google Search"]