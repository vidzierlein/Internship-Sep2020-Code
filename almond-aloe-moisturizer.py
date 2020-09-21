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
browser.get("http://weathershopper.pythonanywhere.com/")

#Validating the successful navigation to the current weather page
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
        # Take screenshot
        browser.save_screenshot('Qxf2_Tutorial.png')
        addToCart = (browser.find_elements_by_xpath('//button[@class="btn btn-primary"]'))
        for each in addToCart:
            each.click()
        print("cold moisturizer")
        
        addToCart = (browser.find_elements_by_xpath('//div[@class="text-center col-4"]'))

        #Determine which moisturizer has the lowest 
        #price or which sunscreen has the lowest price

        productNames=[]
        productPrices=[]
        #iterate through the list of all moisturizers or all conditioners
        for each_item in addToCart:
            item = each_item.text
            print("&&&&",item)
            print(f"item name{item}")
            print(type(item), "++")
            item_element = item.split("\n")
            print(item_element, "**")
            productPrice = (item_element[-2]).split(" ")
            productPrice = int(productPrice[-1])
            productPrices.append(productPrice)
            print("**",productPrice)
            print(type(productPrice), "##")
            productName = (item_element[-3])
            productNames.append(productName)

        print(productNames)
        print(productPrices, "AA")


        #determine the lowest prices moisturizer/suncreen along with the product name
        min_price = 100000000000 
        min_name = ''

        min_prices = []
        aloe_names = []

        for name, price in zip(productNames, productPrices):
            if "aloe" in name.lower():
                print("aloe present")
                aloe_names.append(name)
                min_prices.append(price)
        print(aloe_names)
        print(min_prices)

        for aloe_min_name , aloe_min_price in zip(aloe_names, min_prices):
            if aloe_min_price < min_price:
                min_price = aloe_min_price
                min_name = aloe_min_name

        print(min_name,",", "Rs.",min_price)

        min_prices = []
        almond_names = []

        for name, price in zip(productNames, productPrices):
            if "almond" in name.lower():
                    print("almond present")
                    almond_names.append(name)
                    min_prices.append(price)

        print(almond_names)
        print(min_prices)

        for almond_min_name , almond_min_price in zip(almond_names, min_prices):
            if almond_min_price < min_price:
                min_price = almond_min_price
                min_name = almond_min_name

        print(min_name,",", "Rs.",min_price)
    else:
        print(" Please check the Moisturizer page URL again")
elif inttemperature  > 34:
    submit = (browser.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]"))
    print(submit)
    submit.click()
    if browser.title == "The Best Sunscreens in the World!":
        print("Successful navigation to the Sunscreen page")
        # Take screenshot
        browser.save_screenshot('Qxf2_Tutorial.png')
        addToCart = (browser.find_elements_by_xpath('//button[@class="btn btn-primary"]'))
        for all in addToCart:
            all.click()
        print("hot sunscreen")
        addToCart = (browser.find_elements_by_xpath('//div[@class="text-center col-4"]'))

        #Determine which moisturizer has the lowest 
        #price or which sunscreen has the lowest price

        productNames=[]
        productPrices=[]
        #iterate through the list of all moisturizers or all conditioners
        for each_item in addToCart:
            item = each_item.text
            print("&&&&",item)
            print(f"item name{item}")
            print(type(item), "++")
            item_element = item.split("\n")
            print(item_element, "**")
            productPrice = (item_element[-2]).split(" ")
            productPrice = int(productPrice[-1])
            productPrices.append(productPrice)
            print("**",productPrice)
            print(type(productPrice), "##")
            productName = (item_element[-3])
            productNames.append(productName)

        print(productNames)
        print(productPrices, "AA")


        #determine the lowest prices moisturizer/suncreen along with the product name
        min_price = 100000000000 
        min_name = ''

        min_prices = []
        SPF50_names = []

        for name, price in zip(productNames, productPrices):
            if "spf-50" in name.lower():
                print("SPF-50 sunscreen%%%%%%%")
                SPF50_names.append(name)
                min_prices.append(price)
        print(SPF50_names)
        print(min_prices)

        for SPF50_min_name, SPF50_min_price in zip(SPF50_names, min_prices):
            if SPF50_min_price < min_price:
                min_price = SPF50_min_price
                min_name = SPF50_min_nam

        print(min_name,",", "Rs.",min_price)

        min_prices = []
        SPF30_names = []

        for name, price in zip(productNames, productPrices):
            if "spf-30" in name.lower():
                    print("SPF-30 sunscreen%%%%%%%")
                    almond_names.append(name)
                    min_prices.append(price)

        print(SPF30_names)
        print(min_prices)

        for SPF30_min_name , SPF30_min_price in zip(almond_names, min_prices):
            if SPF30_min_price < min_price:
                min_price = SPF30_min_price
                min_name = SPF30_min_name

        print(min_name,",", "Rs.",min_price)
    else:
        print("Check the url for shopping page")
else:
    print("There is no need for neither suncreen nor moisturizer")

""" addToCart = (browser.find_elements_by_xpath('//div[@class="text-center col-4"]'))

#Determine which moisturizer has the lowest 
#price or which sunscreen has the lowest price

productNames=[]
productPrices=[]
#iterate through the list of all moisturizers or all conditioners
for each_item in addToCart:
    item = each_item.text
    print(f"item name{item}")
    print(type(item), "++")
    item_element = item.split("\n")
    print(item_element, "**")
    productPrice = (item_element[-2]).split(" ")
    productPrice = int(productPrice[-1])
    productPrices.append(productPrice)
    print("**",productPrice)
    print(type(productPrice), "##")
    productName = (item_element[-3])
    productNames.append(productName)

print(productNames)
print(productPrices, "AA")


#determine the lowest prices moisturizer/suncreen along with the product name
min_price = 100000000000 
min_name = ''

min_prices = []
aloe_names = []

for name, price in zip(productNames, productPrices):
   if "aloe" in name.lower():
    print("aloe present")
    aloe_names.append(name)
    min_prices.append(price)
print(aloe_names)
print(min_prices)

for aloe_min_name , aloe_min_price in zip(aloe_names, min_prices):
    if aloe_min_price < min_price:
        min_price = aloe_min_price
        min_name = aloe_min_name

print(min_name,",", "Rs.",min_price)

min_prices = []
almond_names = []

for name, price in zip(productNames, productPrices):
       if "almond" in name.lower():
            print("almond present")
            almond_names.append(name)
            min_prices.append(price)

print(almond_names)
print(min_prices)

for almond_min_name , almond_min_price in zip(almond_names, min_prices):
    if almond_min_price < min_price:
        min_price = almond_min_price
        min_name = almond_min_name

print(min_name,",", "Rs.",min_price) """

    


"""i have taken 2 list, one for name and one for price. i check if the aloe 
      substring  is present in the string, 
      if yes i'll append the product name to product list and its price to price list. 
      after getting all the aloe products, i am 
      checking the min priced product and taking its index. 
      through the index I am getting the product name.
  if price < min_price:
    min_price = price
    min_prices.append(min_price)
    min_name = name
    min_names.append(min_name)
 """
#print(min_names)
#print(min_prices)

time.sleep(3)
browser.close()
browser.quit()
browser.find_element_by_xpath('//button[@onclick ="addToCart(%s,%s)"]'%(low_priced_aloe_moisturiser,str(lowest_aloeProduct))).click().   