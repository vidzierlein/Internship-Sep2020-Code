import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()
# Navigate to Weather Shopper page      
driver.get("http://weathershopper.pythonanywhere.com/")

buy_sunscreen_button = driver.find_element_by_xpath("//button[contains(.,'Buy sunscreens')]")
if buy_sunscreen_button.is_displayed(): 
    print("Buy Sunscreen button is displayed")

buy_moistuzier_button = driver. find_element_by_xpath( "//button[contains(.,'Buy moisturizers')]")
if buy_moistuzier_button.is_displayed():
    print("Buy Moisturizer button is displayed")


driver.close()
driver.quit()