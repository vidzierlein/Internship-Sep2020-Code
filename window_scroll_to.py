
import time
from selenium import webdriver

# Create an instance of Chrome WebDriver
driver = webdriver.Chrome()
# Maximize the browser window
driver.maximize_window()
# Navigate to CNN website
driver.get("https://cnn.com")

time.sleep(1)

driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

time.sleep(3)

driver.close()
driver.quit()