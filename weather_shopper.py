"""
SCOPE:
1) Launch Chrome driver
2) Navigate to http://weathershopper.pythonanywhere.com/
3) PDetermine the temperature from this page
4)Shop for moisturizers if the weather is below 19 degrees. Shop for suncreens if the weather is above 34 degrees.
5) Validate if it has landed on the right page.
6) Take a screenshot
7) Close the browser
"""

import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()
# Navigate to Weather Shopper page      
driver.get("http://weathershopper.pythonanywhere.com/")

# Find the Example table element in the page
temperature = driver.find_element_by_xpath("//span[@id='temperature']")
temperature = temperature.text

temperature = "temperature[0]" + "temperature[1]"
print(temperature)
inttemperature = int(temperature)
#if else condition to determine display of Moisturizer or Suncreen page

if temperature  < 19:
    submit = driver.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]")
    submit.click()
    time.sleep(3)
    driver.get("http://weathershopper.pythonanywhere.com/moisturizer")
    print("cold moisturizer")
else:
    submit = driver.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]")
    submit.click()
    time.sleep(3)
    driver.get("http://weathershopper.pythonanywhere.com/sunscreen")
    print("Hot sunscreen")

# Close the browser       
driver.close()

''' # Create a list to store the text
result_data = []
# Go to each row and get the no of columns and the navigate to column 
# Then get the text from each column
for i in xrange(0,len(rows)):
    # Find no of columns by getting the td elements in each row
    cols = rows[i].find_elements_by_tag_name('td')
    cols_data = []
    for j in xrange(0,len(cols)):
        # Get the text of each field 
        cols_data.append(cols[j].text.encode('utf-8'))           
    result_data.append(cols_data)
# Print the result set
print(result_data)

# Find the name field using xpath with id
name = driver.find_element_by_xpath("//input[@id='name']")
# Send text to the name element using send_keys method
name.send_keys('Avinash')
# Find the email field using xpath without id
email = driver.find_element_by_xpath("//input[@name='email']")
email.send_keys('avinash@qxf2.com')
# Find the phone no field using id
phone = driver.find_element_by_id('phone')
phone.send_keys('9999999999')

# Set a dropdown
driver.find_element_by_xpath("//button[@data-toggle='dropdown']").click()  
time.sleep(1)
# Find the xpath of particular option and click on it
driver.find_element_by_xpath("//a[text()='Male']").click()

# Set a checkbox
checkbox = driver.find_element_by_xpath("//input[@type='checkbox']")
checkbox.click()

# Take screenshot
driver.save_screenshot('Qxf2_Tutorial.png')

# Identify the xpath for Click me button and click on it 
button  = driver.find_element_by_xpath("//button[text()='Click me!']")  
button.click()

# Pause the script for 3 sec
time.sleep(3)

# Verify user is taken to Qxf2 tutorial redirect url
if (driver.current_url== 'http://qxf2.com/selenium-tutorial-redirect'):
    print("Success")
else:
    print("Failure")

# Pause the script for 3 sec
time.sleep(3)

# Close the browser       
driver.close()
        
 '''