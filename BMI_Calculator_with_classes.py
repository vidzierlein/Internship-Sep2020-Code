'''I need three functions
-to get the input(height and weight)
- to caluclate BMI
- to check the range'''
class calculate_my_bmi:
    def user_input(self):
        "Getting height and weight from the user"
        self.height = float(input("Enter your height in m: "))
        self.weight = int(input("Enter your weight in kg: "))
        return self.height, self.weight

    def calculate_bmi(self):
        "Calculate BMI using height and weight"
        self.bmi = self.weight / (self.height * self.height)
        return self.bmi

    def check_bmi_range(self):
        "Check the BMI from a range"
        if self.bmi < 18.5:
            print("Underweight")
        elif self.bmi >= 18.5 and self.bmi <= 24.9:
            print("Normal or Healthy Weight")
        elif self.bmi >= 25 and self.bmi <= 29.9:
           print("Overweight")
        else:
            print("Obese")
    
    

calculate_my_bmi_one = calculate_my_bmi()
calculate_my_bmi_one.user_input()
calculate_my_bmi_one.calculate_bmi()
calculate_my_bmi_one.check_bmi_range()

calculate_my_bmi_two = calculate_my_bmi()
calculate_my_bmi_two.user_input()
calculate_my_bmi_two.calculate_bmi()
calculate_my_bmi_two.check_bmi_range()
