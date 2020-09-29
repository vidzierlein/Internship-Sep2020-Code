import datetime
from selenium import webdriver
import calendar as cal
print(datetime.MAXYEAR)

browser = webdriver.Chrome()
browser.get("https://www.google.com")

print(cal.day_name)