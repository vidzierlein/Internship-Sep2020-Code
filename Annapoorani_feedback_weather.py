

"""
SCOPE:
1) Launch Chrome browser
2) Navigate to http://weathershopper.pythonanywhere.com/
3) Determine the temperature from this page
4) Shop for moisturizers if the weather is below 19 degrees. Shop for suncreens if the weather is above 34 degrees.
5) Validate if it has landed on the right page.
6) Take a screenshot
7) Add all products on page to Cart
8) Create a list of all products in Cart
9) Find the product with the lowest price
10)Display the product with the lowest price along with product name
7) Close the browser
"""

import time
from selenium import webdriver
addToCart = []

def check_title():
    "Check the title of the page"
    #Validating the successful navigation to the current weather page
    if (browser.title == "Current Temperature"):
        print("successful navigation to current weather page")
    else:
        print(" Please check the URL again")

def check_temperature(temperature):
    "check the temperature and clicks the button"
    #if else condition to determine display of Moisturizer or Suncreen page
    if temperature  < 19:
        submit = browser.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]")
        submit.click()
        if browser.title == "The Best Moisturizers in the World!":
            print("Successful navigation to the Moisturizer page")
            print("cold moisturizer")
        else:
            print(" Please check the Moisturizer page URL again")
    elif temperature  > 34:
        submit = (browser.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]"))
        print(submit)
        submit.click()
        if browser.title == "The Best Sunscreens in the World!":
            print("Successful navigation to the Sunscreen page")
            print("hot sunscreen")
        else:
            print("Check the url for shopping page")
    else:
        print("There is no need for neither suncreen nor moisturizer")


def read_temperature():
    "Reads the temperature"
    # store value to 'temperature' variable
    temperature = browser.find_element_by_xpath("//span[@id='temperature']")
    temperature = temperature.text
    temperature = temperature.split()
    print(temperature[-2])
    inttemperature = int(temperature[-2])

    return inttemperature


addToCart = (browser.find_elements_by_xpath('//div[@class="text-center col-4"]'))

#Determine which moisturizer has the lowest
#price or which sunscreen has the lowest price

##productNames=[]
#productPrices=[]
product_condition = ['aloe','almond']
min_price = 100000000000

#iterate through the list of all products on all conditions

browser.find_element_by_xpath('//button[@onclfor each_condition in product_condition]')
print("each_condition i am executing",each_condition)
print(addToCart,"I am addto cart")
for each_item in addToCart:
    print("I am coming inside for loop")
    item = each_item.text
    item_element = item.split("\n")
    product_price = (item_element[-2]).split(" ")
    productPrice = int(productPrice[-1])
    #productPrices.append(productPrice)
    productName = (item_element[-3])
    print("**",productPrice,productName)
    if each_condition in productName.lower():
        if productPrice < min_price:
            min_price = productPrice
            min_name = productName
            min_name = "'"+min_name+"'"
            print(min_price,min_name)        

    print("I am coming to line number 99")
    add = addToCart(%s,%s) %(min_name,min_price)).click()


if __name__ == "__main__":
    # Create an instance of Chrome WebDriver
    browser = webdriver.Firefox()
    # Maximize the browser window
    browser.maximize_window()
    # Navigate to Weather Shopper page
    browser.get("http://weathershopper.pythonanywhere.com/")
    check_title()
    temperature = read_temperature()
    check_temperature(temperature)


