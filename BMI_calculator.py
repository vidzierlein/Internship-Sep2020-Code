'''I need three functions
-to get the input(height and weight)
- to caluclate BMI
- to check the range'''

def user_input():
    "Getting height and weight from the user"
    height = float(input("Enter your height in m: "))
    weight = int(input("Enter your weight in kg: "))
    return height, weight

def calculate_bmi(height, weight):
    "Calculate BMI using height and weight"
    bmi = weight / (height*height)
    return bmi

def check_bmi_range(bmi):
    "Check the BMI from a range"
    if bmi < 18.5:
        return "Underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
        return "Normal or Healthy Weight"
    elif bmi >= 25 and bmi <= 29.9:
        return "Overweight"
    else:
        return "Obese"

if __name__ == "__main__":
    height, weight = user_input()
    print(height, weight)
    bmi = calculate_bmi(height, weight)
    print(round(bmi, 2))
    print(check_bmi_range(bmi))