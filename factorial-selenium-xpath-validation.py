"""
Check for the message after the factorial calculation 
and check that the output is correct mathematically

AUTHOR: Vid Zierlein
Contact: vidhya.zierlein@qxf2.com

SCOPE:
1) Launch Chrome browser
2) Navigate to http://qainterview.pythonanywhere.com/
3) Find the Calculate! button and click on it
4) Check for the validation message showing the task was completed 
and arthmetically correct

5) Close the browser
"""
import time
from selenium import webdriver

#Create an instance of Chrome browser
driver = webdriver.Chrome()
#Maximize the browser window
driver.maximize_window()

#Accept input from user
number = int(input("Enter a number: "))
def factorial_without_recursion(number):
    fact = 1
    while(number > 0):
        fact = fact * number
        number = number - 1
    print('Factorial of', number,'is: '+ str(fact))
    return(fact)
expected_result = factorial_without_recursion(number)
print(expected_result)
#Navigate to python anywere Factorial page
driver.get("http://qainterview.pythonanywhere.com/")
#print('success')
set_textfield = driver.find_element_by_xpath("//input[@type='text']").send_keys(number)

#Find the Calculate! button and click it
button = driver.find_element_by_xpath("//button[@id='getFactorial']").click()
#Pause the script to wait for validation message to load
time.sleep(5)

result_text = driver.find_element_by_xpath("//p[@id='resultDiv']")
#result_message is a variable which stores the message "Factorial of x is y"
result_message = result_text.text
result_message = result_message.split()
print(words)


print(type(words[-1]))
    
if int(words[-1]) == expected_result:
    print("Sucessfully executed the arithmetic")
else:
    print("Arithmetic calculation is incorrect")

driver.close()