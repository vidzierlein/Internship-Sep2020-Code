import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://qxf2.com/selenium-tutorial-main")


name = driver.find_element_by_xpath("//input[@id='name']")  
name.send_keys('vid')

driver.find_element_by_xpath("//input[@name='email']").send_keys('vidzierlein@qxf2.com')

phone = driver.find_element_by_id('phone')
phone.send_keys('1234567890')

button = driver.find_element_by_xpath("//button[text()='Click me!']")  
button.click()

time.sleep(3)

if (driver.current_url== 'https://qxf2.com/selenium-tutorial-redirect'):
    print("Success")
else:
    print("Failure")

driver.close()

        

