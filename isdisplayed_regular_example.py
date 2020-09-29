import time
from selenium import webdriver

if __name__ == "__main__":
    # Create an instance of Chrome WebDriver
    browser = webdriver.Firefox()
    #browser = webdriver.Chrome()
    # Maximize the browser window
    browser.maximize_window()
    # Navigate to Jpetstore page
    #browser.get("https://petstore.octoperf.com/actions/Catalog.action?viewCategory=&categoryId=DOGS")
    browser.get("https://weathershopper.pythonanywhere.com")
    #page_title = 'Current Temperature'

Moisturizer = browser.find_element_by_xpath("//button[contains(.,'Buy moisturizers')]")
print(Moisturizer.text)
if (Moisturizer.text).isDisplayed() == True:
    print("test is passed")


browser.close()
browser.quit()