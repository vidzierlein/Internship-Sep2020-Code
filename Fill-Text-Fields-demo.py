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
search.send_keys("St. Bernard")

submit = driver.find_element_by_xpath("//div[contains(@class,'FPdoLc')]/descendant::input[@aria-label='Google Search']")

if (driver.title == "St. Bernard - Google Search"):
    print("Search results page has launced")
#driver.get("https://www.google.com/search?q=St.+Bernard&hl=en&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiNifG8peDrAhVL63MBHQcZBMQQ_AUoAXoECB0QAw")
#driver.click("//a[@class='q qs'I][text()='Images']")

print("Success")

time.sleep(3)


driver.close()

#//div[contains(@class,"FPdoLc")]/descendant::input[@aria-label="Google Search"]