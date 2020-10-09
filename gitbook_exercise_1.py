'''Write a program to prompt the user for hours 
and rate per hour to compute gross pay.
Take into account that the factory gives the 
employee 1.5 times the hourly rate for hours worked above 40 hours.

Enter Hours: 45
Rate: 10
Pay: 475.0'''

class employee_pay:
    "Employee pay amount"

    def __init__(self):
        self.hours = 0
        self.rate = 0
        self.pay = 0
 
    def user_input(self):
        "Requesting user to input, hours worked and rate of pay"
        self.hours = int(input("Enter the number of hours worked: "))
        self.rate = float(input("Enter your rate of pay: "))    
        return self. hours, self.rate

    def calculate_pay_amount(self):
        "Calculate pay amount"
        if self.hours < 40:
            self.pay = self.hours * self.rate
        else:
            self.pay = self.hours *(self.rate * 1.5)
        print(self.pay)
        return self.pay

employee_pay_1 = employee_pay()
employee_pay_1.user_input()
employee_pay_1.calculate_pay_amount()
