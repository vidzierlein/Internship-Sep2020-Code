
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

def check_title(pagetitle):
    '''checks page title to ensure navigation to the correct page'''
    result_flag = False
    if browser.title == pagetitle:
        result_flag = True
    else:
        result_flag = False
    
    return result_flag

def read_temperature():
    '''reads the temperature on the Current Temperature page'''
    temperature = browser.find_element_by_xpath("//span[@id='temperature']")
    temperature = temperature.text
    temperature = temperature.split()
    inttemperature = int(temperature[-2])
    
    return inttemperature

def check_temperature(current_temperature):
    '''Check the temperature'''
    if current_temperature < 19:
        submit = browser.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]")
        submit.click()
        if check_title("The Best Moisturizers in the World!") == True:
            print("Successful navigation to moisturizer page")
        return "Moisturizer"
    elif current_temperature > 34:
        submit = browser.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]")
        submit.click()
        if check_title("The Best Sunscreens in the World!") == True:
            print("Successful navigation to sunscreen page")
        return "Sunscreen"

def check_minimum_price(product_price):
    "Find the minmum price of the product"
    min_price = 100000000000
    if product_price < min_price:
        min_price = product_price

    return min_price


def add_to_cart(product_condition):
    "Adding the products into the cart"
    products_xpaths = browser.find_elements_by_xpath('//div[@class="text-center col-4"]')
    for each_item in products_xpaths:
        item = each_item.text
        item_element = item.split("\n")
        product_price = (item_element[-2]).split(" ")
        product_price = int(product_price[-1])
        product_name = (item_element[-3])
        if each_condition.lower() in product_name.lower():
            min_price = check_minimum_price(product_price)
            min_name = ""
            min_name = product_name
            min_name = "'"+min_name+"'"
    time.sleep(3)
    browser.find_element_by_xpath('//button[@onclick="addToCart(%s,%s)"]'%(min_name, str(min_price))).click()

    return min_name, min_price

if __name__ == "__main__":
    # Create an instance of Chrome WebDriver
    #browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    # Maximize the browser window
    browser.maximize_window()
    # Navigate to Weather Shopper page
    browser.get("http://weathershopper.pythonanywhere.com")
    #browser.get("http://qxf2.com")
    page_title = 'Current Temperature'
 
    current_temperature = read_temperature()
    time.sleep(1)
    if check_temperature(current_temperature) == "Moisturizer":
        product_condition = ['aloe','almond']
    else:
        product_condition = ['SPF-50', 'SPF-30']

    for each_condition in product_condition:
        product_name,product_price = add_to_cart(each_condition)
        print("%s at a price of Rs.%s has been added in to the cart "%(product_name,product_price))

    time.sleep(1)
    cart = browser.find_element_by_xpath("//button[@class='thin-text nav-link']")
    cart.click()

    table = browser.find_element_by_xpath('//table[@class ="table table-striped"]')
    cart_items = table.find_elements_by_xpath("//tbody/descendant::tr")
    
    for every_tr in cart_items:
        product_name_cart = every_tr.find_element_by_xpath('.//td[1]').text
        product_price_cart = every_tr.find_element_by_xpath(".//td[2]").text
        product_name_cart = "'"+product_name_cart+"'"
        if product_name_cart == product_name:
            if int(product_price_cart) == product_price:
                print("Cart verified")
                
browser.close()