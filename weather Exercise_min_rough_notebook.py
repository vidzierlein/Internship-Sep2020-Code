def lowest_price(productPrices):
    min_price = productPrices[0]
    for price in productPrices:
        if price < min_price:
            min_price = price
    return min_price

def lowest_price_Product(productNames):
    min_name = productNames[0]
    for price in productPrices:
        if price < min_price:
            min_price = price
    return min_price

    for price in productPrices:






>>> prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
>>> for k, v in prices.items():
...     prices[k] = round(v * 0.9, 2)  # Apply a 10% discount
...
>>> prices
{'apple': 0.36, 'orange': 0.32, 'banana': 0.23}



dict(zip([1,2,3,4], [a,b,c,d]))


'''
"""
SCOPE:
1) Launch Chrome browser
2) Navigate to http://weathershopper.pythonanywhere.com/
3) Determine the temperature from this page
4) Shop for moisturizers if the weather is below 19 degrees. Shop for suncreens if the weather is above 34 degrees.
5) Validate if it has landed on the right page.
6) Take a screenshot
7) Close the browser
"""

import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
browser = webdriver.Chrome()
# Maximize the browser window
browser.maximize_window()
# Navigate to Weather Shopper page      
browser.get("http://weathershopper.pythonanywhere.com/sunscreen")

if (browser.title == "Current Temperature"):
    print("successful navigation to current weather page")
else:
    print(" Please check the URL again")

addToCart = []

time.sleep(3)

# store value to 'temperature' variable
temperature = browser.find_element_by_xpath("//span[@id='temperature']")
temperature = temperature.text
temperature = temperature.split()

print(temperature[-2])
inttemperature = int(temperature[-2])
#if else condition to determine display of Moisturizer or Suncreen page

if inttemperature  < 19:
    submit = browser.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]")
    submit.click()
    if browser.title == "The Best Moisturizers in the World!":
        print("Successful navigation to the Moisturizer page")
        addToCart = (browser.find_elements_by_xpath('//button[@class="btn btn-primary"]'))
        for each in addToCart:
            each.click()
        print("cold moisturizer") 
    else:
        print(" Please check the Moisturizer page URL again")
elif inttemperature  > 34:
    submit = (browser.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]"))
    print(submit)
    submit.click()
    namePriceDict={}

    if browser.title == "The Best Sunscreens in the World!":
        print("Successful navigation to the Sunscreen page")
addToCart = (browser.find_elements_by_xpath('//div[@class="text-center col-4"]'))

#print(addToCart)
productNameProductPrice=[]
print(type(productNameProductPrice))
productNameList = []
productPrice=[]
for each_item in addToCart:
    item = each_item.text
    item_element = item.split("\n")
    print("Hi",item_element)
    item_element[-2]
    productPricelist = (item_element[-2]).split(" ")
    print(productPricelist)
    for price in productPricelist:
        Price = int(price)
        productPricelist.append(Price)

print(productPricelist)   
''' productPrice.append(productPricelist[-1])
    print(productPrice)
    minimum_price = min(productPrice) '''


    
# Pause the script for 3 sec
time.sleep(3)

# Close the browser       
browser.close() '''



'''Next file'''
"""
SCOPE:
1) Launch Chrome driver
2) Navigate to http://weathershopper.pythonanywhere.com/
3) Determine the temperature from this page
4)Shop for moisturizers if the weather is below 19 degrees. Shop for suncreens if the weather is above 34 degrees.
5) Validate if it has landed on the right page.
6) Add all products to the Cart
7) Close the browser

b = browser.find_element_by_xpath('//button[@onclick ="addToCart(%s,%s)"]'%(moist,str(low_price))).click()
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
temperature = temperature.split()

print(temperature[-2])
inttemperature = int(temperature[-2])
#if else condition to determine display of Moisturizer or Suncreen page

if inttemperature  < 19:
    submit = driver.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]")
    submit.click()
    time.sleep(1)
    driver.get("http://weathershopper.pythonanywhere.com/moisturizer")
    #print("cold moisturizer")
else:
    submit = driver.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]")
    submit.click()
    time.sleep(1)
    driver.get("http://weathershopper.pythonanywhere.com/sunscreen")
    #print("Hot sunscreen")

AddToCart = driver.find_element_by_xpath(("//button[text()='addToCart!']"))
# Close the browser       
#driver.save_screenshot('screenie.png')
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
© 2020 GitHub, Inc.
Terms
Privacy
Security
Status
Help
Contact GitHub
Pricing
API
Training
Blog
About


