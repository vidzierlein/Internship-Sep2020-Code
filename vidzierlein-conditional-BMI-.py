import time
from selenium import webdriver



#Accept input from user
HeightInMeters = (int(input("Enter your height in cm: "))) / 100
WeightInKg =  (int(input("Enter your weight in kg: ")))

bmi = WeightInKg/(HeightInMeters*HeightInMeters)
bmi = round(bmi,2)
print("Your body mass index is: ", bmi)


if bmi <= 18.5:
    print('BMI is', bmi,'I am underweight.')
    driver = webdriver.Chrome() 
    driver.get("https://www.eatright.org/health/weight-loss/your-health-and-your-weight/healthy-weight-gain")
    time.sleep(2)
    driver.close()

elif bmi > 18.5 and bmi < 25:
    print('BMI is', bmi,'I am in an healthy weight range.')
    driver = webdriver.Chrome() 
    driver.get("https://www.nia.nih.gov/health/maintaining-healthy-weight")
    time.sleep(2)
    driver.close()

elif bmi > 25 and bmi < 30:
    driver = webdriver.Chrome() 
    print('BMI is', bmi,'I am overweight.')
    driver.get("https://caloriecontrol.org/four-steps-to-tackling-overweight/")
    time.sleep(2)
    driver.close()

elif bmi > 30:
    driver = webdriver.Chrome()
    print('BMI is', bmi,'I am obese.')
    driver.get("https://www.mayoclinic.org/diseases-conditions/obesity/diagnosis-treatment/drc-20375749")
    time.sleep(2)
    driver.close()
else:
    print('There is an error with your input')
    print('Please check you have entered whole numbers\n'
              'and decimals were asked.') 

    