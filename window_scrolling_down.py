from selenium import webdriver
import time

browser=webdriver.Firefox()
time.sleep(2)
browser.get("https://en.wikipedia.org")
browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(3)
browser.close()