import time
from selenium import webdriver

browser = webdriver.Chrome()
# Maximize the browser window
browser.maximize_window()
# Navigate to Weather Shopper page
browser.get("http://weathershopper.pythonanywhere.com/moisturizer")  

cart = browser.find_element_by_xpath("//button[@class='thin-text nav-link']")
cart.click()

for product_name in cart:
        
        if product_name == product_name_cart and product_price = product_price_cart
        
table = browser.find_element_by_xpath('//table[@class ="table table-striped"]')
cart_items = table.find_elements_by_xpath("//tbody/descendant::tr")
for every_tr in cart_items:
    product_name = every_tr.find_element_by_xpath('//td[1]').text
    name.append(product_name)
    product_price = every_tr.find_element_by_xpath("//td[2]").text
    price.append(int(product_price))