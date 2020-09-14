"""Fill-Text-Fields

SCOPE:
1) Launch Chrome Driver
2) Navigate to Qxf2 Tutorial page
3) Find Google search field using id, xpath, xpath without id
4) Fill search criteria in the Google search field
5) Close the browser

"""
import time
from selenium import webdriver

#create an instance of Chrome WebDriver
driver = webdriver.Chrome()

# The driver.get method will navigate to a page given by the URL
driver.get("https://www.google.com")

# Check if the title of the page is proper
if(driver.title =="Google"):
    print("Success: Google search page launched successfully")
else:
    print("Failure: Google page Title is incorrect")

# Find the search field using xpath with id
search = driver.find_element_by_xpath("//input[@name='q']")
# KEY POINT: Send text to an element using send_keys method
search.send_keys("qxf2")

#Find the Google Search button using id
submit = driver.find_element_by_xpath("//div[contains(@class,'FPdoLc')]/descendant::input[@aria-label='Google Search']")

print("Success")

# Sleep is one way to wait for things to load
time.sleep(3)

# Close the browser window
driver.close()

