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

# Create an instance of Chrome WebDriver
browser = webdriver.Chrome()
# Maximize the browser window
browser.maximize_window()
# Navigate to Weather Shopper page      
browser.get("http://weathershopper.pythonanywhere.com")

#functions
#check pge title to ensure navigation to the correct page
def check_title(pagetitle):
    '''checks the equality of pape title'''
    if browser.title == "%s" % pagetitle:
        print(browser.title)
        return True
        print("successful navigation to the page")
    else:
        print("wrong page")

check_title("Current Temperature")
check_title("The Best Moisturizers in the World!")

def read_temperature():
    '''Reads the temperature on Current Temperature page'''
    # store value to 'temperature' variable
    temperature = browser.find_element_by_xpath("//span[@id='temperature']")
    temperature = temperature.text
    temperature = temperature.split()
    print(temperature[-2])
    inttemperature = int(temperature[-2])
    print(inttemperature)
    return inttemperature

read_temperature()
def check_temperature():
    if read_temperature() < 19:
        print("moisturizer")
        submit = browser.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]")
        submit.click()
        if check_title("The Best Moisturizers in the World!") == True:
            print("Successful navigation to moisturizer page")
    elif read_temperature() > 34:
        print("sunscreen")
        submit = browser.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]")
        submit.click()
        if check_title("The Best Sunscreens in the World!") == True:
            print("Successful navigation to sunscreen page")

check_temperature()

add_to_cart = browser.find_elements_by_xpath('//div[@class="text-center col-4"]')

min_price = 100000000000
product_condition = ['aloe','almond']
product_names=[]
product_prices=[] 
for each_item in add_to_cart:
    item = each_item.text
    item_element = item.split("\n")
    product_price = (item_element[-2]).split(" ")
    product_price = int(product_price[-1])
    product_prices.append(product_price)
    product_name = (item_element[-3])
    product_names.append(product_name)
    print("**",product_price,product_name, product_names,
product_prices)

for each_condition in product_name.lower():
    for product_name, product_price in zip(product_names, product_prices):
        if product_price < min_price:
            min_price = product_price
            min_name = product_name
            min_name = "'"+min_name+"'"
            print(min_price,min_name, "success")        


#add_to_cart(product_condition)
#addToCart = browser.find_elements_by_xpath('//button[@class="btn btn-primary"] and contains')
#print("success")

#selective_add_to_cart(product_condition[n]
browser.close()