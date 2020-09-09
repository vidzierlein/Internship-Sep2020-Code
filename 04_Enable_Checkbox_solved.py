import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://flatlogic.github.io/awesome-bootstrap-checkbox/demo/")

checkbox = driver.find_element_by_id('checkbox1')
checkbox.click()

time.sleep(3)

driver.close()